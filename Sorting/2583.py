from collections import deque

M, N, K = map(int, input().split())
graph = [[0] * M for _ in range(N)]
ans = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(K):
  sxPos, syPos, exPos, eyPos = map(int, input().split())
  for i in range(sxPos, exPos):
    for j in range(syPos, eyPos):
      if graph[i][j] == 0:
        graph[i][j] = 1

def bfs(xPos, yPos):
  count = 1
  graph[xPos][yPos] = 'X'
  queue = deque()
  queue.append((xPos, yPos))
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= N or ny >= M:
        continue
      if graph[nx][ny] == 0:
        graph[nx][ny] = 'X'
        queue.append((nx, ny))
        count += 1
  ans.append(count)

count = 0
for i in range(N):
  for j in range(M):
    if graph[i][j] == 0:
      bfs(i, j)
      count += 1

print(count)
ans.sort()
for i in range(len(ans)):
  print(ans[i], end=" ")
