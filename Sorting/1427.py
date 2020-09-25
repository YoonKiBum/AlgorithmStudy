data = input()
ans = []

for i in range(len(data)):
  ans.append(data[i])

ans.sort(reverse = True)

for i in range(len(data)):
  print(ans[i], end="")
