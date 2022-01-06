n = int(input())
alphaList = [0] * 26
data = []

for i in range(n):
  data.append(input())


for i in range(n):
  for j in range(len(data[i])):
    n = len(data[i])-j-1
    alpha = ord(data[i][j]) - ord('A')
    alphaList[alpha] += pow(10, n)

mul = 9
result = 0

alphaList.sort(reverse = True)

for i in range(26):
  result += alphaList[i] * mul
  mul -= 1
  if mul == 0:
    break
    
print(result)
