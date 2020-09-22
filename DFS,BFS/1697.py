from collections import deque
visited = [0] * 100001

N, K = map(int, input().split())

def bfs(graph, n, k):
  queue = deque()
  queue.append(n)
  while queue:
    i = queue.popleft()
    if i == k:
      return visited[i]
    for j in [i-1, i+1, 2 * i]:
      if (0 <= j < 100001 ) and visited[j] == 0:
        visited[j] = visited[i] + 1
        queue.append(j)

print(bfs(visited, N, K))
