import heapq
INF = 1001

n, m = map(int, input().split())
graph = [[] for _ in range(1 + n)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start, pos):
    distance = [INF] * (1 + n)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
       
    return distance[pos]
x, y = map(int, input().split())
dist1 = dijkstra(1, x)
dist2 = dijkstra(x, y)
dist3 = dijkstra(y, n)

dist4 = dijkstra(1, y)
dist5 = dijkstra(y, x)
dist6 = dijkstra(x, n)

ans = min(dist1 + dist2 + dist3, dist4 + dist5 + dist6)
if ans >= INF:
    print(-1)
else:
    print(ans)


