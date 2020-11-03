from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for i in range(N):
  graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(xPos, yPos):
  queue = deque()
  queue.append((xPos, yPos))
  visited[xPos][yPos] = 1
  while queue:
    count = 0
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= N or ny >= M:
        continue
      if graph[nx][ny] == 0 and visited[nx][ny] == 0: 
        count += 1
      if graph[nx][ny] != 0 and visited[nx][ny] == 0:
        queue.append((nx, ny))
        visited[nx][ny] = 1
    graph[x][y] -= count
    if graph[x][y] < 0:
      graph[x][y] = 0

count = 0
while True:
  visited = [[0]*M for _ in range(N)]
  count2 = 0
  count3 = 0
  count4 = 0
  for i in range(N):
    for j in range(M):
      if graph[i][j] != 0 and visited[i][j] == 0:
        count2 += 1
        count3 += 1
        if count2 >= 2:
          break
        elif count3 == 0:
          break
        bfs(i, j)
      if graph[i][j] == 0:
        count4 += 1
    if count2 >=2:
      break
  if count3 == 0:
    print(0)
    break
  if count4 == 0:
    print(0)
    break
  if count2 >= 2:
    print(count)
    break
  count += 1
   
  
