import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
graph2 = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)
distance2 = [INF] * (N + 1)
ans = []
for i in range(M):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph2[b].append((a, c))

def dijkstra(start, gr, dis):
  q = []
  dis[start] = 0
  heapq.heappush(q, (0, start))
  while q:
    dist, now = heapq.heappop(q)
    if dis[now] < dist:
      continue
    for i in gr[now]:
      cost = dist + i[1]
      if cost < dis[i[0]]:
        dis[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(X, graph, distance)
dijkstra(X, graph2, distance2)

for i in range(1, len(distance)):
  ans.append(distance[i] + distance2[i])
print(max(ans[1:]))
