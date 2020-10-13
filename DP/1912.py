N = int(input())
data = list(map(int, input().split()))
INF = int(1e9) * -1
sum = [INF] * (1 + N)
sum[0] = data[0]

for i in range(1, N):
  sum[i] = max(sum[i-1] + data[i], data[i])

print(max(sum))
