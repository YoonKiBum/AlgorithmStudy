N = int(input())
data = []
for i in range(N):
  name, kor, eng, math = input().split()
  data.append((name, int(kor), int(eng), int(math)))

data.sort(key = lambda x: ((-x[1]), x[2], (-x[3]), x[0]))

for i in range(N):
  print(data[i][0])
