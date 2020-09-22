from collections import deque
graph = []
queue = deque()
cnt = 0
cnt2 = 0
cnt3 = 0

M, N = map(int, input().split()) # N행 M 열
for i in range(N):
  graph.append(list(map(int, input().split())))

# 상 하 좌 우
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]


def bfs():
  global cnt, cnt2
  while queue:
    for _ in range(len(queue)):
      x, y = queue.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
          continue
        if graph[nx][ny] == 0:
          graph[nx][ny] = 1
          queue.append((nx, ny))
          cnt2 += 1
    cnt += 1

for i in range(N):
  for j in range(M):
    if graph[i][j] == 1:
      queue.append((i, j))
      cnt2 += 1
    elif graph[i][j] == -1:
      cnt3 += 1

bfs()

if N * M - cnt3 == cnt2:
  print(cnt - 1)
else:
  print(-1)
