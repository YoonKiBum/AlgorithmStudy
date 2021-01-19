n = int(input())
data = input()
count = 0
for i in range(len(data)):
  if data[i] == 'L':  
    count += 1

if count == 0:
  print(n)
else:
  print(n-(count//2-1))
