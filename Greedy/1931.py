n = int(input())
data = []

for i in range(n):
  a, b = map(int, input().split())
  data.append((a, b))

data.sort(key = lambda x: (x[1], x[0]))

count = 1
start, end = data[0]

for i in range(1, n):
  a, b = data[i]
  if a >= end:
    end = b
    count += 1

print(count)
