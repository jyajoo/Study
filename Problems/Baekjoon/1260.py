# DFS와 BFS

n, m, v = map(int, input().split(' '))  # n : 정점, m : 간선, v : 시작할 정점 번호

graph = [[0]*(n+1) for _ in range(n+1)]  # 인덱스값 = 정점
visited = [False] * (n+1)  # 방문여부 체크리스트

for i in range(m):  # 간선만큼
    a, b = map(int, input().split(' '))
    graph[a][b] = graph[b][a] = 1  # 두 정점을 이어준다.


def DFS(start):
    visited[start] = True
    print(start, end=" ")
    for i in range(1, n+1):  # 1부터 n까지 검사
        if not visited[i] and graph[start][i] == 1:  # 방문을 하지 않았고, 간선이 있는 곳
            DFS(i)


def BFS(start):
    queue = [start]  # 큐 이용
    visited[start] = False  # DFS에서 방문한 곳을 1로 표시하여서 BFS는 0으로 표시
    while queue:
        start = queue.pop(0)
        print(start, end=" ")
        for i in range(1, n+1):
            if visited[i] and graph[start][i] == 1:
                queue.append(i)
                visited[i] = False


DFS(v)
print()
BFS(v)
