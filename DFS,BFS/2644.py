from collections import deque
N = int(input())
start, end = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(M):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

def bfs(start, end):
  queue = deque()
  queue.append(start)
  cnt = 0
  while queue:
    for _ in range(len(queue)):
      v = queue.popleft()
      if v == end:
        print(cnt)
        return
      for i in graph[v]:
        if not visited[i]:
          queue.append(i)
          visited[i] = True
    cnt += 1
  print(-1)
  return
bfs(start, end)
