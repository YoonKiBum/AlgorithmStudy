from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = []

for i in range(N):
  data = input()
  for j in range(M):
    graph[i].append(data[j])

def bfs(xPos,yPos):
  queue = deque()
  queue.append((xPos, yPos))
  visited = [[0]*M for _ in range(N)]
  visited[xPos][yPos] = 1
  count = -1
  while queue:
    for _ in range(len(queue)):
      x, y = queue.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
          continue
        if graph[nx][ny] == 'L' and visited[nx][ny] == 0: 
          visited[nx][ny] = 1
          queue.append((nx, ny))
    count += 1
  ans.append(count)

for i in range(N):
  for j in range(M):
    if graph[i][j] == 'L':
      bfs(i, j)

print(max(ans))
