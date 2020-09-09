N = int(input())
data = list(map(int, input().split()))
total = 0
total2 = 0
data.sort()

for i in data:
  total += i
  total2 += total


print(total2)
