# #행렬 곱셈

N , M = map(int, input().split(' '))
a = []
b = []
for _ in range(N):
    a.append(list(map(int, input().split(' '))))

M , K = map(int, input().split(' '))
for _ in range(M):
    b.append(list(map(int, input().split(' '))))

result = [[0 for _ in range(K)] for _ in range(N)] #행렬 N*K 크기만큼
for n in range(N):
    for k in range(K):
        for m in range(M):
            result[n][k] += a[n][m] * b[m][k] #!!

for i in result:
    for j in i:
        print(j, end = " ")
    print()