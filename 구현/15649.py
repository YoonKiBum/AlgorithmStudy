from itertools import permutations

n, m = map(int, input().split())
data = []

for i in range(1, n+1):
  data.append(i)

answer = list(permutations(data, m))

for i in range(len(answer)):
  for j in range(0, m):
    print(answer[i][j], end=" ")
  print()
