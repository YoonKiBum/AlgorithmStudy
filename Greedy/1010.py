dp = [0] * 31
dp[0] = 1
dp[1] = 1
 
for i in range(2, 31):
  dp[i] = dp[i-1] * i
 
T = int(input())
for i in range(T):
  n, m = map(int, input().split())
  a = dp[m-n]
  b = dp[m]
  c = dp[n]
 
  print((b//a)//c)
