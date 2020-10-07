from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
  start, end = map(int, input().split())
  graph[start].append(end)
  graph[end].append(start)

def bfs(start, end):
  queue = deque()
  queue.append(start)
  visited = [0] * (N + 1)
  cnt = 0
  while queue:
    for _ in range(len(queue)):
      v = queue.popleft()
      if v == end:
        return cnt
      for i in graph[v]:
        if not visited[i]:
          queue.append(i)
          visited[i] = True
    cnt += 1

result = []

for i in range(1, N + 1):
  ans = 0
  for j in range(1, N + 1):
    if i == j:
      continue
    else:
      ans += bfs(i, j)
  result.append(ans)

print(result.index(min(result)) + 1)
