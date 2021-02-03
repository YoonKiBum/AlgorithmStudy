from collections import deque
n = int(input())
q = deque()
for i in range(n):
    num = int(input())
    if num != 0:
        q.append(num)
    else:
        q.pop()

print(sum(q))
