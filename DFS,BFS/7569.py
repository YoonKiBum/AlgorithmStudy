from collections import deque

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
queue = deque()
cnt = 0 # 1 확인
cnt2 = 0 # -1 확인
cnt3 = 0 # 0 확인
count = 0 # 정답을 담을 변수

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

for i in range(H):
  for j in range(N):
    for k in range(M):
      if graph[i][j][k] == 1: # 해당 칸에 토마토가 있는 경우
        queue.append((i, j, k))
        cnt += 1
      elif graph[i][j][k] == -1: 
        cnt2 += 1
      
def bfs():
  global count
  while queue:
    count += 1
    for _ in range(len(queue)):
      z, x, y = queue.popleft()
      for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if nx < 0 or ny < 0 or nz < 0 or nx >= N or ny >= M or nz >= H: # 범위를 벗어나는 경우
          continue
        if graph[nz][nx][ny] == 0:
          graph[nz][nx][ny] = 1
          queue.append((nz, nx, ny))

if cnt2 == N * M * H: # 전체가 -1인 경우
  print(-1)
elif cnt + cnt2 == N * M * H: # 시작부터 다 익은 경우
  print(0)
else:
  bfs()
  for i in range(H):
    for j in range(N):
      for k in range(M):
        if graph[i][j][k] == 0:
          cnt3 += 1
  if cnt3 != 0:
    print(-1)
  else:
    print(count - 1)
