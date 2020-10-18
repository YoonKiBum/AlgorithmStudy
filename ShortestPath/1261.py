import heapq
M, N = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(N)]
distance = [[INF] * M for _ in range(N + 1)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
  data = input()
  for j in range(M):
    graph[i].append(int(data[j]))

def dijkstra(start):
  q = []
  distance[start[0]][start[1]] = 0
  heapq.heappush(q, (graph[0][0], (0,0)))
  while q:
    dist, pos = heapq.heappop(q)
    for i in range(4):
      nx = pos[0] + dx[i]
      ny = pos[1] + dy[i]
      if nx < 0 or ny < 0 or nx >= N or ny >= M:
        continue
      if distance[nx][ny] < dist:
        continue
      cost = dist + graph[nx][ny]
      if cost < distance[nx][ny]:
        distance[nx][ny] = cost
        heapq.heappush(q, (cost, (nx, ny)))

dijkstra((0, 0))
print(distance[N-1][M-1])
