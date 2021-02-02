from collections import deque

tc = int(input())
for i in range(tc):
    q = deque()
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    a = 1
    for p in priority:
        q.append((a, p))
        a += 1
    i = 0
    count = 1
    while i < len(q):
        check = True
        for j in range(i, len(q)):
            if q[i][1] < q[j][1]:
                a, p = q.popleft()
                q.append((a, p))
                check = False
                break
        if not check:
            i = 0
        else:
            a, p = q.popleft()
            if a == 1 + m:
                print(count)
                break
            else:
                count += 1
            i = 0
    
