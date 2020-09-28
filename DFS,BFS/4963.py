from collections import deque

# 상 하 좌 우 좌상단, 좌하단, 우상단, 우하단
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
ans = []

while True:
  W, H = map(int, input().split()) # H가 행 W가 열
  if H == 0 and W == 0:
    break
  graph = []
  for i in range(H):
    graph.append(list(map(int, input().split())))
  
  def bfs(xPos, yPos):
    queue = deque()
    queue.append((xPos, yPos))
    while queue:
      x, y = queue.popleft()
      for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= H or ny >= W:
          continue
        if graph[nx][ny] == 1:
          graph[nx][ny] = graph[x][y] + 1
          queue.append((nx, ny))
   
  cnt = 0
  for i in range(H):
    for j in range(W):
      if graph[i][j] == 1:
        bfs(i, j)
        cnt += 1
  print(cnt)
  
