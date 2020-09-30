from collections import deque
import copy

N = int(input())
graph = [[] for _ in range(N)]

for i in range(N):
  data = input()
  for j in range(N):
    graph[i].append(data[j])

testgraph = copy.deepcopy(graph)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(xPos, yPos, t):
  if t == 1: # R 찾기
    graph[xPos][yPos] = 0
    queue = deque()
    queue.append((xPos, yPos))
    while queue:
      x, y = queue.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
          continue
        if graph[nx][ny] == 'R':
          graph[nx][ny] = 0
          queue.append((nx, ny))
  elif t == 2: # G 찾기
    graph[xPos][yPos] = 0
    queue = deque()
    queue.append((xPos, yPos))
    while queue:
      x, y = queue.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
          continue
        if graph[nx][ny] == 'G':
          graph[nx][ny] = 0
          queue.append((nx, ny))
  elif t == 3: # B 찾기
    graph[xPos][yPos] = 0
    queue = deque()
    queue.append((xPos, yPos))
    while queue:
      x, y = queue.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
          continue
        if graph[nx][ny] == 'B':
          graph[nx][ny] = 0
          queue.append((nx, ny)) 

def bfs2(xPos, yPos, t):
  if t == 1: # R혹은 G인 경우
    testgraph[xPos][yPos] = 0
    queue = deque()
    queue.append((xPos, yPos))
    while queue:
      x, y = queue.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
          continue
        if testgraph[nx][ny] == 'R' or testgraph[nx][ny] == 'G':
          testgraph[nx][ny] = 0
          queue.append((nx, ny))
  elif t == 2: # B인경우
    testgraph[xPos][yPos] = 0
    queue = deque()
    queue.append((xPos, yPos))
    while queue:
      x, y = queue.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
          continue
        if testgraph[nx][ny] == 'B':
          testgraph[nx][ny] = 0
          queue.append((nx, ny))

count = 0
for i in range(N):
  for j in range(N):
    if graph[i][j] == 'R':
      bfs(i, j, 1)
      count += 1
    elif graph[i][j] == 'G':
      bfs(i, j, 2)
      count += 1
    elif graph[i][j] == 'B':
      bfs(i, j, 3)
      count += 1

count2 = 0
for i in range(N):
  for j in range(N):
    if testgraph[i][j] == 'R' or testgraph[i][j] == 'G':
      bfs2(i, j, 1)
      count2 += 1
    elif testgraph[i][j] == 'B':
      bfs2(i, j, 2)
      count2 += 1

print(count, count2)
