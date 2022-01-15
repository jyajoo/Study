#체스판 다시 칠하기

n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]
chess = []

for i in range(n-7):
    for j in range(m-7): #8*8크기의 체스판을 위해 행,열 고정
        cntW = 0
        cntB = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y)%2 == 0:
                    if arr[x][y] != "W":
                        cntW += 1
                    if arr[x][y] != "B":
                        cntB += 1

                else:
                    if arr[x][y] != "B":
                        cntW += 1
                    if arr[x][y] != "W":
                        cntB += 1
        chess.append(cntW)
        chess.append(cntB)

print(min(chess))