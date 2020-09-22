from collections import deque
T = int(input())

for i in range(T):
  M, N, K = map(int, input().split())
  graph = [[0] * M for _ in range(N)]
  queue = deque()
  count = 0
  
  for _ in range(K):
    start, end = map(int, input().split())
    graph[end][start] = 1
  
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  def dfs(graph):
    while queue:
      x, y = queue.popleft()
      for j in range(4):
        nx = dx[j] + x
        ny = dy[j] + y
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
          continue
        if graph[nx][ny] == 1:
          graph[nx][ny] = 0
          queue.append((nx, ny))

  for j in range(N):
    for k in range(M):
      if graph[j][k] == 1:
        graph[j][k] = 0
        queue.append((j, k))
        dfs(graph)
        count += 1
  
  print(count)
