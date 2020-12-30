from collections import deque
t = int(input()) # 테스트 케이스

for _ in range(t):
  n = int(input())
  graph = [[False] * (1 + n) for _ in range(1 + n)]
  indegree = [0] * (1 + n)
  data = list(map(int, input().split()))
  
  for i in range(n):
    for j in range(i+1, n):
      graph[data[i]][data[j]] = True
      indegree[data[j]] += 1

  m = int(input())
  for _ in range(m):
    a, b  = map(int, input().split())
    if graph[a][b]:
      graph[a][b] = False
      graph[b][a] = True
      indegree[b] -= 1
      indegree[a] += 1
    else: # 이어지지 않은 경우
      graph[a][b] = True
      graph[b][a] = False
      indegree[b] += 1
      indegree[a] -= 1

  def topology_sort():
    result = []
    q = deque()

    for i in range(1, 1 + n):
      if indegree[i] == 0:
        q.append(i)
    
    certain = True
    cycle = False

    for i in range(n):
      if len(q) == 0:
        cycle = True
        break 

      if len(q) >= 2:
        certain = False
        break

      now = q.popleft()
      result.append(now)
      
      for i in range(1, n+1):
        if graph[now][i]:
          indegree[i] -= 1
          if indegree[i] == 0:
            q.append(i)
    
    if cycle:
      print("IMPOSSIBLE")
    elif not certain:
      print("?")
    else:
      for i in result:
        print(i, end=" ")
      print()

  topology_sort()
