# 바이러스 (bfs 너비우선탐색)

n = int(input())  # 컴퓨터의 수(정점의 개수)
m = int(input())  # 연결된 쌍의 수(간선의 개수)
graph = [[0]*(n+1) for _ in range(n+1)]  # 인덱스값을 정점으로 생각
visited = [False] * (n+1)  # 정점을 방문하였는지
count = 0  # 바이러스 걸린 컴퓨터의 수

for i in range(m):
    a, b = map(int, input().split(' '))
    graph[a][b] = graph[b][a] = 1  # 둘 사이가 연결되어있다면 1


def BFS(start):
    queue = [start]  # 큐 이용
    visited[start] = True
    while queue:
        start = queue.pop(0)
        for i in range(1, n+1):
            if not visited[i] and graph[start][i] == 1:
                queue.append(i)
                visited[i] = True


BFS(1)
for i in visited:
    if i:
        count += 1
print(count-1)  # 1번 컴퓨터 제외

####################################################################
# 바이러스 (dfs 깊이우선탐색)

n = int(input())
m = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for i in range(m):
    a, b = map(int, input().split(' '))
    graph[a][b] = graph[b][a] = 1


def DFS(start):
    visited[start] = True
    for i in range(1, n+1):
        if not visited[i] and graph[start][i] == 1:
            DFS(i)


DFS(1)
for i in visited:
    if i:
        count += 1
print(count-1)
