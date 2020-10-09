N = int(input())
data = []

for i in range(N):
  data.append(list(map(int, input().split())))

for i in range(1, N):
  for j in range(len(data[i])):
    if j == 0: # 맨 앞인 경우
      data[i][j] = data[i-1][j] + data[i][j]
    elif j == i: # 맨 뒤인 경우
      data[i][j] =  data[i-1][j-1] + data[i][j]
    else: # 그 외의 경우
      data[i][j] = max(data[i-1][j-1], data[i-1][j]) + data[i][j]

print(max(data[N - 1]))
