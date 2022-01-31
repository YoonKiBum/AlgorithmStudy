n = int(input())
data = list(map(int, input().split()))
dp = [0] * n
dp[0] = data[0]

for i in range(1, n):
  dp[i] = max(data[i], dp[i-1] + dp[0])
  for j in range(i//2+1):
    dp[i] = max(dp[i], dp[j] + dp[i-j-1])

print(dp[n-1])
