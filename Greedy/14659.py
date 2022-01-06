n = int(input())

data = list(map(int, input().split()))
maximum = 0
cnt = 0
ans = 0

for i in range(n):
  if data[i] > maximum:
    maximum = data[i]
    cnt = 0
  else:
    cnt += 1
  if ans < cnt:
    ans = cnt

print(ans)  
