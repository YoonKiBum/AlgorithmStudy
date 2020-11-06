N = int(input())
data_Plus = []
data_Minus = []
one = 0
zero = 0
ans = []

for i in range(N):
  input_data = int(input())
  if input_data > 1:
    data_Plus.append(input_data)
  elif input_data < 0:
    data_Minus.append(input_data)
  elif input_data == 1:
    one += 1
  elif input_data == 0:
    zero += 1

data_Plus.sort()
data_Minus.sort(reverse = True)

for _ in range(len(data_Plus)):
  if len(data_Plus) <= 1:
    break
  ans.append(data_Plus[len(data_Plus)-1] * data_Plus[len(data_Plus)-2])
  data_Plus.pop()
  data_Plus.pop()

for _ in range(len(data_Minus)):
  if len(data_Minus) <= 1:
    break
  ans.append(data_Minus[len(data_Minus)-1]* data_Minus[len(data_Minus)-2])
  data_Minus.pop()
  data_Minus.pop()

if len(data_Plus) == 1:
  ans.append(data_Plus[0]) 
  data_Plus.pop()

while one >= 1:
  ans.append(1)
  one -= 1

if len(data_Minus) == 1 and zero >= 1:
  ans.append(0)
  data_Minus.pop()

if len(data_Minus): 
  ans.append(data_Minus[0])
  data_Minus.pop()

print(sum(ans))
