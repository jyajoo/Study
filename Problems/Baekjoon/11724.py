# 연결 요소의 개수(bfs, 시간초과)

import sys
n, m = map(int, input().split(' '))  # n : 정점의 개수, m : 간선의 개수
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a][b] = graph[b][a] = 1  # 간선의 개수만큼 정점끼리 연결해준다


def BFS(start):
    queue = [start]
    while queue:
        start = queue.pop(0)
        for i in range(1, n+1):
            if not visited[i] and graph[start][i] == 1:  # 방문하지 않았고, 간선이 존재한다면
                queue.append(i)
                visited[i] = True


count = 0  # 연결 요소의 개수
for i in range(1, n+1):
    if not visited[i]:  # 방문하지 못한 곳을 시작 정점으로 하여서 개수를 세어준다.
        BFS(i)
        count += 1
print(count)
##############################################################################################
# 연결 요소의 개수(bfs)


n, m = map(int, sys.stdin.readline().split(' '))
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split(' '))
    graph[a][b] = graph[b][a] = 1


def BFS(start):
    queue = [start]
    while queue:
        start = queue.pop(0)
        for i in range(1, n+1):
            if not visited[i] and graph[start][i] == 1:  # 방문하지 않았고, 간선이 존재한다면
                queue.append(i)
                visited[i] = True


count = 0
for i in range(1, n+1):
    if not visited[i]:
        BFS(i)
        count += 1
print(count)
##############################################################################################
# 연결 요소의 개수(dfs, 런타임 에러(recursionerror))

n, m = map(int, input().split(' '))
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a][b] = graph[b][a] = 1


def DFS(start):
    visited[start] = True
    for i in range(1, n+1):
        if not visited[i] and graph[start][i] == 1:
            DFS(i)


count = 0
for i in range(1, n+1):
    if not visited[i]:
        DFS(i)
        count += 1
print(count)

############################################################################
# 연결 요소의 개수(dfs)

sys.setrecursionlimit(10000)  # python이 정한 최대 깊이를 더 깊게 변경해줌

n, m = map(int, sys.stdin.readline().split(' '))
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split(' '))
    graph[a][b] = graph[b][a] = 1


def DFS(start):
    visited[start] = True
    for i in range(1, n+1):
        if not visited[i] and graph[start][i] == 1:
            DFS(i)


count = 0
for i in range(1, n+1):
    if not visited[i]:
        DFS(i)
        count += 1
print(count)
