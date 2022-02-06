from collections import deque

def bfs(start, distance):
  count = 0
  visited = [0] * (n+1)
  q = deque()
  q.append((start, 0))
  visited[start] = True

  while q:
    v, dist = q.popleft()
    for i, cost in graph[v]:
      if dist == 0:
        cost2 = cost
      else:
        cost2 = min(cost, dist)
      if not visited[i] and cost2 >= distance:
        q.append((i, cost2))
        visited[i] = True
        count += 1
  return count

n, q = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

for _ in range(q):
  k, v = map(int, input().split())
  print(bfs(v, k))
