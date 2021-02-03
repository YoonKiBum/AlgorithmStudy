n, m = map(int, input().split())
r, c, d = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def turn_left():
    global d
    d = (d-1) % 4

count = 1
x, y = r, c
graph[x][y] = 2 # 방문처리를 2로 함

while True:
    check = False
    for i in range(4):
        turn_left()
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                count += 1
                graph[nx][ny] = 2
                x, y = nx, ny
                check = True
                break
    if not check: # 4방향을 확인했음에도 청소할 공간이 없는 경우
        nx = x - dx[d]
        ny = y - dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 2:
                x, y = nx, ny
            elif graph[nx][ny] == 1:
                print(count)
                break
        else:
            print(count)
            break

