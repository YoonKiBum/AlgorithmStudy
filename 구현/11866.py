from collections import deque

n, k = map(int, input().split())
q = deque()

for i in range(1, n+1):
  q.append(i)

print("<", end="")
i = 0
while True:
  i += 1
  if i != k:
    v = q.popleft()
    q.append(v)
  else:
    v = q.popleft()
    if (q):
      print(v, end=", ")
      i = 0
    else:
      print(v, end=">")
      break


