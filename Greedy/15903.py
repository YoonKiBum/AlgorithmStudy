n, m = map(int, input().split())
data = list(map(int, input().split()))

while True:
  if m <= 0:
    break
  data.sort()
  m -= 1
  x = data.pop(0)
  y = data.pop(0)
  data.append(x+y)
  data.append(x+y)

print(sum(data))
