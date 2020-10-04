from collections import deque

K = int(input()) # test case
for _ in range(K):
  V, E = map(int, input().split())
  graph = [[] for _ in range(V + 1)]
  visited = [0] * (V + 1)
  c = [0] * (V + 1)
  for i in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

  def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
      v = queue.popleft()
      for i in graph[v]:
        if not visited[i]:
          if visited[v] == 1:
            visited[i] = 2
          elif visited[v] == 2:
            visited[i] = 1
          queue.append(i)
        elif visited[i] == visited[v]:
          return 0
    return 1
    
  check = False
  for i in range(V):
    if visited[i] == 0: # 아직 방문하지 않은 경우
      ans = bfs(i)
      if ans == 0: # 이분안되는 경우 check 를 True로 재정의
        check = True 
        break

  if check == True:
    print("NO")
  else:
    print("YES")
      

  
