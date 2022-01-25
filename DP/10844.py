n = int(input())
data = [[0] * 10 for _ in range(n)]

for i in range(1, 10):
  data[0][i] = 1

for i in range(1, n):
  for j in range(10):
    if 1 <= j <= 8:
      data[i][j] = data[i-1][j-1] + data[i-1][j+1]
    elif j == 0:
      data[i][j] = data[i-1][j+1]
    elif j == 9:
      data[i][j] = data[i-1][j-1]

print(sum(data[n-1][0:])%1000000000)
