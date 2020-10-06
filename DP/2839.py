N = int(input())
arr = [3, 5]

d = [1e9] * (N + 1)
d[0] = 0

for i in range(2):
  for j in range(arr[i], N + 1):
    d[j] = min(d[j], d[j - arr[i]] + 1)

if d[N] == 1e9:
  print(-1)
else:
  print(d[N])

