N = int(input())
data = list(map(int, input().split()))

M = int(input())
a = list(map(int, input().split()))
data.sort()

def Binary_search(start, end, target):
  if start > end:
    return None
  mid = int((start + end) / 2)
  if data[mid] == target:
    return 1
  elif data[mid] > target:
    return Binary_search(start, mid - 1, target)
  elif data[mid] < target:
    return Binary_search(mid + 1, end, target)

for i in range(M):
  if Binary_search(0, N-1, a[i]) == None:
    print(0, end=" ")
  else:
    print(1, end=" ")
 
