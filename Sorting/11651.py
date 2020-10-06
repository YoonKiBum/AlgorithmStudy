N = int(input())
data = []

for _ in range(N):
  xPos, yPos = map(int, input().split())
  data.append((xPos, yPos))

data.sort(key = lambda x: x[0])
data.sort(key = lambda x: x[1])

for i in range(N):
  print(data[i][0], data[i][1])
