# 늑대와 양

r, c = map(int, input().split(' '))  # 목장의 크기
farm = []

for i in range(r):
    farm.append(list(input()))

X, Y = [-1, 0, 1, 0], [0, -1, 0, 1]  # 늑대의 좌우, 상하 확인
safe = True  # 늑대가 양에 인접할 수 있는 지

# . : 빈칸, S : 양, W : 늑대
for i in range(r):
    for j in range(c):
        if farm[i][j] == "W":
            for k in range(4):
                dx, dy = i + X[k], j + Y[k]
                if dx < 0 or dy < 0 or dx >= r or dy >= c:  # 범위 밖을 벗어나는 경우
                    continue  # 넘어가기
                elif farm[dx][dy] == "S":  # 양과 인접한다면
                    safe = False
        elif farm[i][j] == "S":
            continue
        else:
            farm[i][j] = "D"  # 울타리 설치

if safe:
    print(1)
    for i in farm:
        print("".join(i))
else:
    print(0)
