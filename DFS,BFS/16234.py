from collections import deque
import sys
input = sys.stdin.readline 

N, L, R = map(int, input().split())
graph = []
for i in range(N):
  graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(xPos, yPos):
  q = deque()
  q.append((xPos, yPos))
  visited[xPos][yPos] = 1
  count = 1
  sum = graph[xPos][yPos]
  arr = [(xPos, yPos)]
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 그래프의 범위를 벗어나지 않은경우
      if 0 <= nx < N and 0 <= ny < N: 
        # 방문한 곳이 아니고 차의 절댓값이 L, R 사이일때
        if visited[nx][ny] == 0 and L <= abs(graph[nx][ny]-graph[x][y]) <= R:
          visited[nx][ny] = 1
          sum += graph[nx][ny]
          count += 1
          q.append((nx, ny))
          arr.append((nx, ny))

  if count > 1: # count가 2 이상인 경우
    ans = sum // count
    for a, b in arr: # 해당 지역에 인구 이동
      graph[a][b] = ans
    return True
  return False
      
      
count = 0
while True:
  visited = [[0]*N for _ in range(N)] # N행 N열짜리 visited리스트
  flag = False # 인구 이동할 칸의 유무를 체크하는 플레그 False로 초기화
  for i in range(N):
    for j in range(N):
      if visited[i][j] == 0 and bfs(i, j) == True: # 방문하지 않았고 bfs의 반환값이 참이라면
        flag = True
  if flag == False: # 인구이동할 칸이 없는 경우
    break
  elif flag == True: # 인구이동한 칸이 있는 경우 count를 하나 증가
    count += 1

print(count)
