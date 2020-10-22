from collections import deque

F, S, G, U, D = map(int, input().split())
move = []
move.append(U)
move.append(D*-1)
data = [-1] * (1+F)
def bfs(start):
  queue = deque()
  queue.append(start)
  data[start] = 0
  while queue:
    p = queue.popleft()
    for i in range(2):
      np = p + move[i]
      if np <= 0 or np > F:
        continue
      if data[np] == -1:
        data[np] = data[p] + 1
        queue.append(np)
bfs(S)
if S == G:
  print(0)
elif data[G] == -1:
  print("use the stairs")
else:
  print(data[G])
