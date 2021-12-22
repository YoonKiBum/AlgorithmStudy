n, k = map(int, input().split())
data = []
ans = 0

for _ in range(n):
    a = int(input())
    data.append(a)

data.sort(reverse = True)
for x in data:
    if k >= x:
        ans += k // x
        k %= x
        

print(ans)       
