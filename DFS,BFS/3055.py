from collections import deque
R, C = map(int, input().split())
graph = [[] for _ in range(R)]
queue = deque()

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(R):
  data = input()
  for j in range(C):
    graph[i].append(data[j])
    if graph[i][j] == '*':
      queue.append((i, j))

for i in range(R):
  for j in range(C):
    if graph[i][j] == 'S':
      queue.append((i, j))

def bfs():
  cnt = 0
  while queue:
    for _ in range(len(queue)):
      x, y = queue.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= R or ny >= C:
          continue
        if graph[nx][ny] == '.' and graph[x][y] == '*':
          graph[nx][ny] = '*'
          queue.append((nx, ny))
        elif graph[nx][ny] == '.' and graph[x][y] == 'S':
          graph[nx][ny] = 'S'
          queue.append((nx, ny))
        if graph[nx][ny] == 'D' and graph[x][y] == 'S':
          print(cnt + 1)
          return 
    cnt += 1
  print("KAKTUS")
  return
bfs()
