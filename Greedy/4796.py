count = 1
while True:
  l, p, v = map(int, input().split())
  if l == 0 and p == 0 and v == 0:
    break
  ans = (v // p)*l
  if (v % p) > l:
    ans += l
  elif (v % p) != 0 and (v % p) <= l:
    ans += (v % p)
  print("Case ",end='')
  print(count, end=': ')
  print(ans)
  count += 1
