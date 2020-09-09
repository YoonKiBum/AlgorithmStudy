N = int(input())
count = 0

while True:
  if N == 0:
    break;
  elif N <= 2:
    count = -1
    break
  elif N % 5 == 0:
    N -= 5
    count += 1
  elif N % 5 != 0 and N >= 3:
    N -= 3
    count += 1


print(count)
  
