from itertools import combinations

space = []
graph = []
teacher = []
check = False

N = int(input())

for i in range(N):
  graph.append(list(input().split()))
  for j in range(N):
    if graph[i][j] == 'X':
      space.append((i, j))
    elif graph[i][j] == 'T':
      teacher.append((i, j))

      
def direction(xPos, yPos, dir): # 학생 못찾으면 참
  if dir == 0: # 상
    while xPos >= 1:
      xPos -= 1
      if graph[xPos][yPos] == 'O':
        return False
      elif graph[xPos][yPos] == 'S':
        return True
  elif dir == 1: # 하
    while xPos <= N - 2:
      xPos += 1
      if graph[xPos][yPos] == 'O':
        return False
      elif graph[xPos][yPos] == 'S':
        return True
  elif dir == 2: # 좌
    while yPos >= 1:
      yPos -=1
      if graph[xPos][yPos] == 'O':
        return False
      elif graph[xPos][yPos] == 'S':
        return True
  else: # 우
    while yPos <= N - 2:
      yPos += 1
      if graph[xPos][yPos] == 'O':
        return False
      elif graph[xPos][yPos] == 'S':
        return True
  return False


def process(): # 학생 못찾으면 참, 찾으면 거짓 반환
  for x,y, in teacher:
    for i in range(4):
      if direction(x, y, i): # 학생 못찾으면 참
        return True
  return False # 학생을 찾으면 False


for data in combinations(space, 3):
  for x, y in data:
    graph[x][y] = 'O'
    if not process(): # 학생을 못찾으면 process 참 반환
      check = True
      break
  for x,y in data:
    graph[x][y] = 'X'

if check:
  print("YES")
else:
  print("NO")

