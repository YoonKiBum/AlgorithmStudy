def find(num, start, last):
  while last >= start:
    mid = (start + last) // 2
    if data2[mid] == num:
      return mid
    elif data2[mid] > num:
      last = mid - 1
    else:
      start = mid + 1

n = int(input())
data = list(map(int, input().split()))
data2 = set(data)
data2 = list(data2)
data2.sort()


for i in range(n):
  print(find(data[i], 0, len(data2)-1), end=" ")
