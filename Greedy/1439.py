data = input()
num = int(data[0])
flag = False
count0 = 0
count1 = 0

if num == 0:
  flag = False
  count0 += 1
elif num == 1:
  flag = True
  count1 += 1

for i in range(1, len(data)):
  a = int(data[i])
  if flag == False and a == 1:
    count1 += 1
    flag = 1
  elif flag == True and a == 0:
    count0 += 1
    flag = 0

print(min(count0, count1))
