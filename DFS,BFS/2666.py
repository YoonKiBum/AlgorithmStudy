from collections import deque

N = int(input())
graph = [[] * N for _ in range(N)]
result = []
count = 0

for i in range(N):
  input_data = input()
  for j in range(N):
    data = int(input_data[j])
    graph[i].append(data)

# 상 하 좌 우 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(xPos,yPos):
  count2 = 0
  queue = deque()
  queue.append((xPos, yPos))
  graph[xPos][yPos] = 'C'
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= N or ny >= N:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = 'C'
        queue.append((nx, ny))
        count2 += 1
  result.append(count2)

for i in range(N):
  for j in range(N):
    if graph[i][j] == 1:
      bfs(i, j)
      count += 1

print(count)
result.sort()
for i in range(len(result)):
  print(result[i] + 1)
