import copy
n = int(input())
graph = [[] for _ in range(n+1)]
data = list(map(int, input().split()))
for i in range(n):
    if data[i] == -1: # 부모가 -1인 경우 루트노드로 설정
        root = i
        continue
    graph[data[i]].append(i) # 루트노드가 아닌경우 해당 그래프의 점에 연결
start = int(input())

def dfs(graph, visited, v): # dfs 방식으로 탐색
    global count
    visited[v] = True # 방문처리
    if len(graph[v]) == 0: # 리프 노드의 개수를 셈
        count += 1
    for i in graph[v]: # 방문처리하지 않은 노드를 재귀의 방식으로 dfs 탐색
        if not visited[i]:
            dfs(graph, visited, i)
    return count

def remove(tempgraph, graph, visited, v): # 입력받은 수의 자식노드를 제거해나가는 함수 dfs 방식 응용
    visited[v] = True
    for i in range(n): # 그래프를 조회하며 dfs 방식으로 탐색한 노드들을 tempgraph에서 삭제
        for j in range(len(graph[i])):
            if graph[i][j] == v:
                tempgraph[i].remove(v)
    for i in graph[v]:
        if not visited[i]:
            remove(tempgraph, graph, visited, i)

if start != root: # 지우기 시작할 노드가 root가 아닌경우
    tempgraph = copy.deepcopy(graph) # graph를 복사하여 tempgraph생성
    count = 0
    visited = [0] * (1 + n)
    remove(tempgraph, graph, visited, start)

    count = 0
    visited = [0] * (1 + n)
    print(dfs(tempgraph, visited, root))
else: # 지우기 시작할 노드가 root인 경우 그냥 0을 출력함
    print(0)
