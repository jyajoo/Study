# 상근이의 여행
import sys


def BFS(start):
    queue = [start]
    cnt = 0
    while queue:
        start = queue.pop(0)
        for i in range(1, n+1):
            if not visited[i] and plane[start][i] == 1:
                queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt  # 정점을 이동할 때마다 개수를 세어줌


t = int(sys.stdin.readline())  # 테스트 케이스의 수
for _ in range(t):
    # n : 국가(정점)의 수, m : 비행기(간선)의 종류
    n, m = map(int, sys.stdin.readline().split(' '))
    plane = [[0]*(n+1) for _ in range(n+1)]
    visited = [False] * (n+1)

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split(' '))
        plane[a][b] = plane[b][a] = 1  # 두 국가를 왕복하는 비행기 표시(그래프)

    print(BFS(1)-1)  # 모든 정점을 방문하는 최소 개수는 1을 빼주어야 한다.

########################################################################################
# 상근이의 여행

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split(' '))
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split(' '))
    print(n-1)  # 따라서, 모든 정점을 방문하는 최소 간선의 개수는 n개의 정점을 가질 때, n-1개이다.

# 신장 트리, 최소 신장 트리의 개념
