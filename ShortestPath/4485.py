import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = []

while True:
  N = int(input())
  if N == 0:
    break
  distance = [[INF] * (1 + N) for _ in range(N)]
  graph = [list(map(int, input().split())) for _ in range(N)]
  
  def dijkstra(x, y):
    q = []
    heapq.heappush(q, (0, (x, y)))
    distance[x][y] = 0 
    while q:
      dist, now = heapq.heappop(q)
      if distance[now[0]][now[1]] < dist:
        continue
      for i in range(4):
        nx = now[0] + dx[i]
        ny = now[1] + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
          continue
        cost = dist + int(graph[nx][ny])
        if cost < int(distance[nx][ny]):
          distance[nx][ny] = cost
          heapq.heappush(q, (cost, (nx, ny)))

  dijkstra(0, 0)
  ans.append(distance[N-1][N-1] + graph[0][0])

for i in range(len(ans)):
  print("Problem", i+1, end=": ")
  print(ans[i])
