N = int(input())
data = [0] * 10001
for i in range(N):
  data[i] = int(input())

d = [0] * 10001
d[0] = data[0]
d[1] = data[0] + data[1]
d[2] = max(data[0] + data[1], data[0] + data[2], data[1] + data[2])

for i in range(3, N):
  d[i] = max(d[i-1], data[i] + data[i-1] + d[i-3], data[i] + d[i-2])

print(d[N-1])
