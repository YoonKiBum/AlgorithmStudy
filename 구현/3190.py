from collections import deque

N = int(input())
graph = [[0]*N for _ in range(N)]
apple = int(input())
for i in range(apple): # 사과 삽입
  a, b = map(int, input().split())
  graph[a-1][b-1] = 1
m  = int(input())
movement = []
for i in range(m):
  a, b = input().split()
  movement.append((int(a),b))

# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def direction(dir, c):
  if c == 'L':
    dir = (dir-1) % 4
  else:
    dir = (dir+1) % 4
  return dir

def solution():
  index = 0
  count = 0
  x, y = 0, 0
  queue = deque()
  queue.append((x, y))
  graph[x][y] = 2
  dir = 0
  while True:
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] != 2:
      if graph[nx][ny] == 0:
        graph[nx][ny] = 2
        queue.append((nx, ny))
        px, py = queue.popleft()
        graph[px][py] = 0
      elif graph[nx][ny] == 1:
        graph[nx][ny] = 2
        queue.append((nx, ny))
    else:
      count += 1
      return count
    x, y = nx, ny
    count += 1
    if index < m and count == movement[index][0]:
      dir = direction(dir, movement[index][1])
      index += 1
print(solution())
