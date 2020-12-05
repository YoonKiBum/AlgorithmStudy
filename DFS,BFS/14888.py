from itertools import permutations

def calc(arr):
  prev = int(arr[0])
  for i in range(1, len(arr)-1):
    if arr[i].isdigit() == False:
      if arr[i] == '+':
        prev += int(arr[i+1])
      elif arr[i] == '-':
        prev -= int(arr[i+1])
      elif arr[i] == '//':
        if prev >= 0:
          prev = prev // int(arr[i+1])
        else:
          prev *= -1
          prev = prev // int(arr[i+1])
          prev *= -1
      elif arr[i] == '*':
        prev *= int(arr[i+1])
  return prev

N = int(input())
num = list(map(int, input().split()))
numOfA, numOfB, numOfC, numOfD = map(int, input().split())

x = []
while True:
  if numOfA > 0:
    x.append('+')
    numOfA -= 1
  if numOfB > 0:
    x.append('-')
    numOfB -= 1
  if numOfC > 0:
    x.append('*')
    numOfC -= 1
  if numOfD > 0:
    x.append('//')
    numOfD -= 1
  if numOfA == 0 and numOfB == 0 and numOfC == 0 and numOfD == 0:
    break

maximum = int(1e9)*-1
minimum = int(1e9)

for xx in list(permutations(x, N-1)):
  j = 0
  arr = []
  for i in range(N-1):
    arr.append(str(num[i]))
    arr.append(str(xx[j]))
    j += 1
  arr.append(str(num[-1]))
  result = calc(arr)
  maximum = max(maximum, result)
  minimum = min(minimum, result)

print(maximum)
print(minimum)
