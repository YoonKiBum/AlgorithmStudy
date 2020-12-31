def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

g = int(input())
p = int(input())
parent = [0] * (1 + g)

for i in range(1, 1 + g):
  parent[i] = i

count = 0
for _ in range(1, 1 + p):
  x = int(input())
  data = find_parent(parent, x)
  if data != 0:
    union_parent(parent, data, data-1)
    count += 1
  else:
    break

print(count)

