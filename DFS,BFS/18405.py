from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = []
data = []

N, M = map(int, input().split())
for i in range(N):
  graph.append(list(map(int, input().split())))
  for j in range(N):
    if graph[i][j] != 0:
      data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

S, X, Y = map(int, input().split())

while q:
  virus, s_time, xPos, yPos = q.popleft()
  if S == s_time:
    break
  for i in range(4):
    nx = xPos + dx[i]
    ny = yPos + dy[i]
    if nx >= 0 and ny >= 0 and nx <= N-1 and ny <= N-1:
      if graph[nx][ny] == 0:
        graph[nx][ny] = virus
        q.append((virus, s_time + 1, nx, ny))

print(graph[X-1][Y-1])
