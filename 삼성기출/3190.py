N = int(input())
graph = [[0]*N for _ in range(N)]
apple = int(input())
movement = []
for i in range(apple):
  a, b = map(int, input().split())
  graph[a-1][b-1] = 1 # 문제에서 맨 좌측 위가 1, 1 이라고 하였기 때문
 
move = int(input())
for i in range(move):
  a, b = input().split()
  movement.append((int(a), b))
 
# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
 
def turn(dir, x): # 다음 방향을 정하는 함수
  if x == 'D':
    dir = (dir -1) % 4
  elif x == 'L':
    dir = (dir+1) % 4
  return dir
 
def game():
  x = 0; y = 0
  graph[x][y] = 2 # 맨 처음 뱀이 0, 0 에 있으므로 해당 지역을 뱀이 있는것으로 표시
  snake = [(x, y)] # 뱀의 현재 좌표를 담는 리스트
  count = 0
  dir = 0 # 맨 처음 방향인 동쪽을 0으로 설정
  index = 0
  while True:
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] != 2:  # 벽이 아니거나 뱀이 있는 지역이 
      if graph[nx][ny] == 0: # 사과 없는 지역인 경우
        count += 1
        graph[nx][ny] = 2
        snake.append((nx, ny))
        prev_x, prev_y = snake.pop(0)
        graph[prev_x][prev_y] = 0
      elif graph[nx][ny] == 1: #사과 있는 지역
        count += 1
        graph[nx][ny] = 2
        snake.append((nx, ny))
      if index < move and count == movement[index][0]:
        dir = turn(dir, movement[index][1])
        index += 1
      x = nx
      y = ny
    else:
      return count
 
print(game()+1)

