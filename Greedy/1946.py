N = int(input())
data = []
count = 0

for i in range(N):
  k = int(input())
  for i in range(k):
    test_A, test_B = map(int, input().split())
    data.append((test_A, test_B))
  sort_list = sorted(data, key = lambda x: x[1])
  min = 1e9
  for i in range(k):
    if sort_list[i][0] <= min:
      min = sort_list[i][0]
    else:
      count += 1
  print(k-count)
  count = 0
  data=[]
