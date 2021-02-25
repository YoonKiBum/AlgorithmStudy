from collections import deque

n, m = map(int, input().split())
max = 100001
visited = [0] * max
move = [-1, 1]
def bfs():
    q = deque()
    q.append(n)
    count = 0
    visited[n] = 1
    if 2*n < max and not visited[2*n]:
        visited[2*n] = 1
        q.append(2*n)
    if visited[m] != 0:
        print(visited[m] - 1)
        return
    while q:
        pos = q.popleft()
        if visited[m] != 0:
            print(visited[m] - 1)
            return
        if 2*pos < max and not visited[2*pos]:
            visited[2*pos] = visited[pos]
            q.append(2*pos)
        for i in range(2):
           npos = pos + move[i]
           if 0 <= npos < max:
               if not visited[npos]:
                   visited[npos] = visited[pos] + 1
                   q.append(npos)

bfs()



