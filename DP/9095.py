tc = int(input())
data = []
for i in range(tc):
  data.append(int(input()))

d = [0] * 31
d[1] = 1; d[2] = 2; d[3] = 4
for i in range(4, 31):
  d[i] = d[i-1] + d[i-2] + d[i-3]

for i in range(len(data)):
  print(d[data[i]])
