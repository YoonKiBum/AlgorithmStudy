from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = []
for i in range(N):
  graph.append(list(map(int, input().split())))
  for j in range(N):
    if graph[i][j] == 9:
      graph[i][j] = 2
      start = (i, j)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
  queue = deque()
  queue.append((a, b))
  visit = [[-1] * N for _ in range(N)]
  visit[a][b] = 0
  eat = []
  while queue:
    xPos, yPos = queue.popleft()
    for i in range(4):
      nx = xPos + dx[i]
      ny = yPos + dy[i]
      if nx < 0 or ny < 0 or nx >= N or ny >= N:
        continue
      if visit[nx][ny] == -1: # 아직 방문 안한지역의 경우
        if graph[nx][ny] <= graph[a][b]:
          queue.append((nx, ny))
          visit[nx][ny] = visit[xPos][yPos] + 1
        if graph[nx][ny] < graph[a][b] and graph[nx][ny] != 0:
          eat.append((nx, ny, visit[nx][ny]))
  if not eat:
    return -1, -1, -1
  eat.sort(key = lambda x: (x[2], x[0], x[1]))
  return eat[0][0], eat[0][1], eat[0][2]
exp = 0
cnt = 0

while True:
  x, y = start[0], start[1]
  nx, ny, dist = bfs(x, y)
  if nx == -1:
    break
  graph[nx][ny] = graph[x][y]
  graph[x][y] = 0
  cnt += dist
  exp += 1
  start = (nx, ny)
  if exp == graph[nx][ny]: # 경험치가 현재 크기랑 같으면
    exp = 0
    graph[nx][ny] += 1

print(cnt)
