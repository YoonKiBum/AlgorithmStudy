from itertools import combinations
from collections import deque

import copy

N, M = map(int, input().split())
graph = []
blank = []
virus = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
  graph.append(list(map(int, input().split())))
  for j in range(M):
    if graph[i][j] == 0: # 빈칸인 경우
      blank.append((i, j))
    elif graph[i][j] == 2: # 바이러스인 경우
      virus.append((i, j))

def bfs():
  cnt = 0
  testGraph = copy.deepcopy(graph)
  queue = deque(virus)
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= N or ny >= M:
        continue
      elif testGraph[nx][ny] == 0:
        testGraph[nx][ny] = 2
        queue.append((nx, ny))
  
  for i in range(N):
    for j in range(M):
      if testGraph[i][j] == 0:
        cnt += 1
  return cnt

maximum = 0

for data in combinations(blank, 3):
  for x, y  in data:
    graph[x][y] = 1
  maximum = max(maximum, bfs())
  for x, y in data:
    graph[x][y] = 0

print(maximum)
