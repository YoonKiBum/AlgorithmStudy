n = int(input())
data = [300, 60, 10]
data2 = [0, 0, 0]

if n % 10 != 0:
  print(-1)
else:
  for i in range(len(data)):
    if n >= data[i]:
      data2[i] += n // data[i]
      n %= data[i]
  strdata2 = map(str, data2) # join을 이용해서 출력해주기 위해서는 str 형태로 바꿔줘야함 
  print(' '.join(strdata2))  # join을 이용해서 공백을 기준으로 
