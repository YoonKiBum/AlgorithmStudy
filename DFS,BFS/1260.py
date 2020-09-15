from collections import deque

n, m, v = map(int, input().split())
graph = [[] * n for _ in range(n + 1)]
visited = [False] * (n + 1)

def dfs(graph, visited, start):
  visited[start] = True
  print(start, end=" ")
  for i in graph[start]:
    if not visited[i]:
     dfs(graph, visited, i)

def bfs(graph, visited, start):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end=" ")
    for i in graph[v]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)
  
for _ in range(m):
  start, end = map(int, input().split())
  graph[start].append(end)
  graph[end].append(start)

for i in range(len(graph)):
  graph[i].sort()

dfs(graph, visited, v)
visited = [False] * (n + 1) # 다시 초기화
print("")
bfs(graph, visited, v)
print("")

