N = int(input())
a = list(map(int, input().split()))
data = [0] * N

for i in range(N):
  for j in range(i):
    if a[i] > a[j] and data[j] > data[i]:
      data[i] = data[j]
  data[i] += 1
  
print(max(data))
