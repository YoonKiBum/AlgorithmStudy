from collections import deque
N = int(input())
K = int(input())
visited = [False] * (N + 1)
graph = [[] * N for _ in range(N + 1)]

for i in range(K):
  start, end = map(int, input().split())
  graph[start].append(end)
  graph[end].append(start)

def dfs(graph, visited):
  queue = deque()
  queue.append(1)
  count = 0
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if visited[i] == 0:
        count += 1
        visited[i] = True
        queue.append(i)
  return (count - 1)

print(dfs(graph, visited))
