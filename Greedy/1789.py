n = int(input())
 
count = 0
ans = 0
for i in range(1, n):
  ans += i
  count += 1
  if ans > n:
    count -= 1
    break
 
print(count)
