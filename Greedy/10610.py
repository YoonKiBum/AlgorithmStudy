s = list(map(str, input()))
s.sort(reverse = True)
 
temp = ""
for i in range(len(s)):
  temp += s[i]
 
temp = int(temp)
 
if temp % 10 != 0 or temp % 3 != 0:
  print(-1)
else:
  print(temp)
