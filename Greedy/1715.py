import heapq

n = int(input())
q = []
for i in range(n):
  data = int(input())
  heapq.heappush(q, data)

total = 0
for i in range(n-1):
  mid = 0
  a = heapq.heappop(q)
  b = heapq.heappop(q)
  mid = (a+b)
  total += mid
  heapq.heappush(q, mid)
  
print(total)
