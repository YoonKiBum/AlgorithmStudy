import sys
from collections import deque 

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        result[i] = result[v] + 1 
        visited[i] = True
        queue.append(i)

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
result = [0] * (N + 1)
visited = [False] * (N + 1)

for i in range(M):
  start, end = map(int, sys.stdin.readline().rstrip().split())
  graph[start].append(end)

bfs(graph, X, visited)
count = 0

for i in range(1, len(result)):
  if K == result[i]:
    print(i)
    count += 1

if count == 0:
  print(-1)
