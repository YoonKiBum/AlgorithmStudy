from collections import deque

def bfs(graph, i, j):
  q = deque()
  q.append((i, j))
  count = 1
  graph[i][j] = 0
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= n:
        continue
      if graph[nx][ny] == 1:
        q.append((nx, ny))
        graph[nx][ny] = 0
        count += 1
  ans.append(count)

n = int(input())
graph = []
ans = []
for _ in range(n):
  graph.append(list(map(int, input())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      bfs(graph, i, j)
      count += 1

print(count)
ans.sort()

for a in ans:
  print(a)
