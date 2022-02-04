from collections import deque
n,k=map(int,input().split())
visited=[0]*100001
q=deque()
q.append(n)
count=0
visited[n]=1
while q:
  x=q.popleft()
  if x==k:
    break
  for next in x-1,x+1,x*2:
    if next < 0 or next >= 100001:
      continue
    if not visited[next]:
      q.append(next)
      visited[next]=visited[x] + 1
print(visited[k]-1)
