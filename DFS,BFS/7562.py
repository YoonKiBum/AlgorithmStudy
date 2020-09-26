from collections import deque
T = int(input())

for _ in range(T):
  N = int(input())
  graph = [[0] * N for _ in range(N)]
  queue = deque()
  sxPos, syPos = map(int, input().split())
  queue.append((sxPos, syPos))
  exPos, eyPos = map(int, input().split())

  dx = [-1, -2, -2, -1, 1, 2, 2, 1]
  dy = [-2, -1, 1, 2, 2, 1, -1, -2]

  count = 0
  def bfs():
    if sxPos == exPos and syPos == eyPos:
      print(0)
      return
    while queue:
      global count
      count += 1
      for _ in range(len(queue)):
        x, y = queue.popleft()
        for i in range(8):
          nx = x + dx[i]
          ny = y + dy[i]
          if nx <  0 or ny < 0 or nx >= N or ny >= N:
            continue
          if graph[nx][ny] == 0:
            graph[nx][ny] = 'a'
            queue.append((nx, ny))
          if graph[exPos][eyPos] == 'a':
            print(count)
            return

  bfs()
