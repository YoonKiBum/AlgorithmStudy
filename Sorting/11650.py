N = int(input())
data = []

for i in range(N):
  start, end = map(int, input().split())
  data.append((start, end))

data.sort(key = lambda x: x[1])
data.sort(key = lambda x: x[0])

for i in range(N):
  print(data[i][0], data[i][1])
