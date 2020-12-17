N, C = map(int, input().split())
data = []
for i in range(N):
  data.append(int(input()))

data.sort()

start = 1 # 공유기 사이 거리 최솟값
end = data[-1] - data[0] # 공유기 사이 거리 최댓값
ans = []

while start <= end:
  prev = data[0]
  mid = (start + end) // 2
  count = 1
  for i in range(1, N):
    if prev + mid <= data[i]:
      prev = data[i]
      count += 1
  if count >= C:
    start = mid + 1
    ans.append(mid)
  else:
    end = mid - 1

print(max(ans))
    
        
