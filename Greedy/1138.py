N = int(input())
data = list(map(int, input().split()))
ans = []

for i in range(N): 
  ans.insert(data[N-i-1], N-i)  

for i in range(N):
  print(ans[i], end=' ')

