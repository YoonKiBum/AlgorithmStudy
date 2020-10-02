from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
queue = deque()
c = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
  data = input()
  for j in range(M):
    graph[i].append(data[j])
    if graph[i][j] == 'R':
      rx, ry = i, j
      graph[rx][ry] = '.' 
    elif graph[i][j] == 'B':
      bx, by = i, j
      graph[bx][by] = '.'
queue.append((rx, ry, bx, by))
c.append((rx, ry, bx, by))

def bfs():
  cnt = 0
  while queue:
    for _ in range(len(queue)):
      rx, ry, bx, by = queue.popleft()
      if graph[rx][ry] == 'O':
        print(cnt)
        return
      for i in range(4):
        nrx, nry, nbx, nby = rx, ry, bx, by
        while True:
          nrx += dx[i]
          nry += dy[i]
          if graph[nrx][nry] == 'O':
            break
          elif graph[nrx][nry] == '#':
            nrx -= dx[i]
            nry -= dy[i]
            break
        while True:
          nbx += dx[i]
          nby += dy[i]
          if graph[nbx][nby] == 'O':
            break
          elif graph[nbx][nby] == '#':
            nbx -= dx[i]
            nby -= dy[i]
            break
        if graph[nbx][nby] == 'O':
          continue
        if nrx == nbx and nby == nry:
          if abs(rx - nrx) + abs(ry - nry) > abs(bx - nbx) + abs(by - nby):
            nrx -= dx[i]
            nry -= dy[i]
          else:
            nbx -= dx[i]
            nby -= dy[i] 
        if (nrx, nry, nbx, nby) not in c:
          queue.append((nrx, nry, nbx, nby))
          c.append((nrx, nry, nbx, nby))
    if cnt >= 10:
      print(-1)
      return
    cnt += 1
  print(-1)
  return 

bfs()      
          
