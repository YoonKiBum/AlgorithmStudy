N = int(input())
data = []

for i in range(N):
  age, name = input().split()
  data.append((int(age), name))

data.sort(key = lambda x: x[0])

for i in range(N):
  print(data[i][0], data[i][1])
