data = input()
array = ["U", "C", "P", "C"]
for i in range(len(data)):
  if data[i] == array[0]:
    array.pop(0)
  if len(array) == 0:
      break
if len(array) == 0:
  print("I love UCPC")
else:
  print("I hate UCPC")
  
