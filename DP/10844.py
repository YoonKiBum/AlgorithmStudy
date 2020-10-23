N = int(input())
data = [[1] * 10 for _ in range(N)]

for i in range(1, N):
  for j in range(0, 10): 
    if 1 <= j <= 8:
      data[i][j] = data[i-1][j-1] + data[i-1][j+1]
    elif j == 9:
      data[i][j] = data[i-1][j-1]
    elif j == 0:
      data[i][j] = data[i-1][j+1]

print(sum(data[N-1][1:])%1000000000)
