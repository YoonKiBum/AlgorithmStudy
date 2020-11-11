n = input()
length = len(n)
left = []
right = []

for i in range(length//2):
  left.append(int(n[i]))

for i in range(length//2, length):
  right.append(int(n[i]))

if sum(left) == sum(right):
  print("LUCKY")
else:
  print("READY")
