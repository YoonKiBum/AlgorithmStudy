from collections import deque

N, M = map(int, input().split())
graph = [[] * M for _ in range(N)] # N 행 M 열인 리스트 graph 생성

for i in range(N): # 붙여서 입력 받음
  input_data = input()
  for j in range(M):
    data = int(input_data[j]) 
    graph[i].append(data)

# 상하좌우의 형태
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(xPos, yPos):
  queue = deque()
  queue.append((xPos, yPos))
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= N or ny >= M:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))

bfs(0, 0)
print(graph[N- 1][M - 1])

