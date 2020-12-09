import heapq
q = []
N = int(input())
for i in range(N):
  heapq.heappush(q, (int(input())))

sum = 0
while len(q) > 1:
  temp1 = heapq.heappop(q)
  temp2 = heapq.heappop(q)
  heapq.heappush(q, (temp1+temp2))
  sum += temp1+temp2
print(sum)
