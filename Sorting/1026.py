N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sorted_B = sorted(B, reverse = True)
A.sort()

ans = 0
for i in range(N):
  ans += (A[i] * B[B.index(sorted_B[i])])
  
print(ans)
