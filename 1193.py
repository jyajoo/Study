# 분수 찾기 # 메모리 초과

n = int(input())
arr = []
num = 1

while (len(arr) != n):

    if num % 2 == 0:
        x = 1
        y = num
        for j in range(num):
            arr.append((x, y))
            x += 1
            y -= 1
            if len(arr) == n:
                break

    else:
        x = num
        y = 1
        for j in range(num):
            arr.append((x, y))
            x -= 1
            y += 1
            if len(arr) == n:
                break

    num += 1

print("%d/%d" % (arr[-1][0], arr[-1][1]))

#############################################
# 분수 찾기_2
a = int(input())  # 입력 받은 수
cnt = 0
cross = 1
while True:
    b = a - cnt   # 새 대각선에서 입력받은 수가 몇 번째인지 확인
    cnt += cross  # 총 개수
    if a <= cnt:  # 총 개수보다 입력받은 수가 작다면, 해당 대각선 중에 위치함을 의미
        if cross % 2 == 1:
            x = cross
            y = 1
            for _ in range(b - 1):
                x -= 1
                y += 1
        elif cross % 2 == 0:
            x = 1
            y = cross
            for _ in range(b - 1):
                x += 1
                y -= 1
        print(x, end="/")
        print(y)
        break
    cross += 1

#############################################
# 분수 찾기_3
a = int(input())

cross = cnt = 1
while a > cnt:
    cross += 1
    cnt += cross

gap = cnt - a
if cross % 2 == 0:
    x = cross - gap
    y = gap + 1

elif cross % 2 == 1:
    x = gap + 1
    y = cross - gap

print(x, end="/")
print(y)
