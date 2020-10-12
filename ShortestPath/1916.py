import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())
graph = [[] * (1 + M) for _ in range(1 + N)]
distance = [INF] * (1 + N)

for i in range(M):
  a, b, c = map(int, input().split())
  graph[a].append((b,c))

start, end = map(int, input().split())

def dickstra(start):
  q = []
  distance[start] = 0
  heapq.heappush(q, (0, start))
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dickstra(start)

print(distance[end])
