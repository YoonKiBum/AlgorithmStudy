n = int(input())
data = []
for _ in range(n):
  data.append(int(input()))

count = 0
for i in range(2, n+1):
  if data[n-i] >= data[n-i+1]:
    count += (data[n-i] - data[n-i+1] + 1)
    data[n-i] = data[n-i] - (data[n-i] - data[n-i+1] + 1)
    
print(count)
