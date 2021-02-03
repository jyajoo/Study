# 좌표 정렬하기
n = int(input())
result = []
for _ in range(n):
    x, y = map(int, input().split(' '))
    result.append((x, y))
result.sort(key=lambda x: (x[0], x[1]))

for i in result:
    print(i[0], i[1])
