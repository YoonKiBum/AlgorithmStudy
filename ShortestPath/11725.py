from collections import deque
N = int(input())
graph = [[] for _ in range(1+N)]
visited = [0] * (1+N)
parent = [0] * (1+N)
for i in range(N-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(start, visited):
  queue = deque()
  queue.append(start)
  visited[start] = 1
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = 1
        parent[i] = v

bfs(1, visited)
for i in range(2, len(parent)):
  print(parent[i])
