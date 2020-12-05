from itertools import combinations
 
def compute(data):
  answer = 0
  for i in range(len(house)):
    a, b = house[i]
    temp = int(1e9)
    for x, y in data:
      temp = min(temp, abs(x - a) + abs(y - b))
    answer += temp
  return answer
 
N, M = map(int, input().split())
town = []
house = []
store = []
 
for i in range(N):
  town.append(list(map(int, input().split())))
  for j in range(N):
    if town[i][j] == 1:
      house.append((i, j))
    elif town[i][j] == 2:
      store.append((i, j))
 
ans = int(1e9)
for data in combinations(store, M):
  ans = min(ans, compute(data))
 
print(ans)
