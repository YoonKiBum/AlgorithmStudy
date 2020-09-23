from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
cnt = 0

def bfs(graph,visited, start):
  queue = deque()
  queue.append(start)
  visited[start] = True
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)

for i in range(M):
  start, end = map(int, input().split())
  graph[start].append(end)
  graph[end].append(start)

for i in range(1, len(visited)):
  if visited[i] == False:
    bfs(graph, visited, i)
    cnt += 1

print(cnt)
