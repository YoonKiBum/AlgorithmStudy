n = 5; r = 3; totalCnt = 0
a = [1, 2, 3, 4, 5]
isSelected = [0] * n
numbers = [0] * r

def perm(cnt):
  global totalCnt, n, r

  if(cnt == r):
    totalCnt += 1
    print(numbers)
    return
  
  for i in range(n):
    if isSelected[i]:
      continue
    isSelected[i] = 1
    numbers[cnt] = a[i]
    perm(cnt + 1)
    isSelected[i] = 0

def comb(cnt, start):
  global totalCnt, n, r

  if(cnt == r):
    totalCnt += 1
    print(numbers)
    return

  for i in range(start, n):
    numbers[cnt] = a[i]
    comb(cnt + 1, i + 1)

def subs(cnt):
  global totalCnt, n, r
  
  if(cnt == n):
    for i in range(n):
      if(isSelected[i]):
        print(a[i], end="")
      else:
        print("X", end="")
    print()
    totalCnt += 1
    return

  isSelected[cnt] = 1
  subs(cnt + 1)
  isSelected[cnt] = 0
  subs(cnt + 1)
  
totalCnt = 0
perm(0)
print(totalCnt)

print()

totalCnt = 0
comb(0, 0)
print(totalCnt)

print()

totalCnt = 0
subs(0)
print(totalCnt)


