n = int(input())
route = list(map(int, input().split()))
amount = list(map(int, input().split()))

price = amount[0]
ans = 0
i = 1
ro = route[0]
while True:
  if i == n-1:
    ans += price * ro
    break
  if price < amount[i]:
    ro += route[i]
  else:
    ans += price * ro
    price = amount[i]
    ro = route[i]
  i += 1

print(ans)
