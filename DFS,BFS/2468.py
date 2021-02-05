from collections import deque

n = int(input())
graph = []
max = 0
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > max: # 그래프에 입력된 값 중 최댓값 찾음
            max = graph[i][j]

def bfs(xPos, yPos, value, visited):
    q = deque()
    q.append((xPos, yPos))
    visited[xPos][yPos] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n: # 그래프의 영역을 벗어나지 않고
                if graph[nx][ny] > value and visited[nx][ny] == 0: # 방문하지 않은 지역이고 잠기지 않은지역이면 bfs수행
                    visited[nx][ny] = 1
                    q.append((nx, ny))
   
maximum = 0

#비가 안오는 0부터 최댓값 전까지 조회(최댓값은 모두 잠기므로 안전영역이 무조건 0임 조회할 필요 없음)
for a in range(max):
    visited = [[0] * n for _ in range(n)] # 비가 오는 매 높이 마다 bfs를 수행해야하므로 매번 visited를 초기화 
    ans = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > a and visited[i][j] == 0: # 방문하지 않고 비가 온 곳보다 높은 지역이면 bfs 수행
                bfs(i, j, a, visited)
                ans += 1 
    if maximum < ans: # 안전영역의 최댓값을 구함
        maximum = ans
print(maximum)
                
               
