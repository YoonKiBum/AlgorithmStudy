A, B, C = map(int, input().split())

if B >= C:
  print(-1)
else:
  ans = int(A / (C - B)) + 1
  print(ans)
