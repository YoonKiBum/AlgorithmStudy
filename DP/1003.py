tc = int(input())
data = []
for i in range(tc):
  data.append(int(input()))

zc = [1, 0]
oc = [0, 1]

for i in range(2, 41):
  zc.append(zc[i-1] + zc[i-2])
  oc.append(oc[i-1] + oc[i-2])

for i in range(tc):
  print(zc[data[i]], oc[data[i]])
