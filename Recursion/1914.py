N = int(input())
ans = []

def HaniTower(num, fromi, by, to):
  if num == 1:
    ans.append((fromi, to))
  else:
    HaniTower(num-1, fromi, to, by)
    ans.append((fromi, to))
    HaniTower(num-1, by, fromi, to)    

if N <= 20:
  HaniTower(N, 1, 2, 3)
elif N > 20:
  answer = 2 ** N - 1
  print(answer)

if N <= 20:
  length = len(ans)
  print(length)
  for i in range(length):
    print(ans[i][0], ans[i][1])

