from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(input()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 1

def bfs(graph, x, y):
  global result
  q = deque()
  visited = graph[x][y]
  q.append((x, y, visited))
  q = set(q)
  while q:
    x, y, vis = q.pop()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if graph[nx][ny] not in vis:
          q.add((nx, ny, vis + graph[nx][ny]))
          result = max(result, len(vis) + 1)

bfs(graph, 0, 0)
print(result)

