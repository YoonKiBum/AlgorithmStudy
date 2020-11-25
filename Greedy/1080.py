N, M = map(int, input().split())
data = [[] for _ in range(N)]
data2 = [[] for _ in range(N)]
check = [[0]*M for _ in range(N)]

def swich(x, y):
  for i in range(x, x+3):
    for j in range(y, y+3):
      if check[i][j] == 1:
        check[i][j] = 0
      else:
        check[i][j] = 1

for i in range(N):
  inputdata = input()
  for j in range(M):
    data[i].append(int(inputdata[j]))

for i in range(N):
  inputdata = input()
  for j in range(M):
    data2[i].append(int(inputdata[j]))

for i in range(N):
  for j in range(M):
    if data[i][j] != data2[i][j]:
      check[i][j] = 1

count = 0

if N >= 3 and M >= 3:
  for i in range(N-3+1):
    for j in range(M-3+1):
      if check[i][j] == 1:
        swich(i, j)
        count += 1
  ans = 0
  for i in range(N):
    ans += sum(check[i])
  if ans == 0:
    print(count)
  else:
    print(-1)
else:
  ans = 0
  for i in range(N):
    ans += sum(check[i])
  if ans == 0:
    print(0)
  else:
    print(-1)
