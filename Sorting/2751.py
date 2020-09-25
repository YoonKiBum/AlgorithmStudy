N = int(input())
data = []

for i in range(N):
  data.append(int(input()))

data.sort()

for i in range(N):
  print(data[i])
