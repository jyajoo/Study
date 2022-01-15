# 풍선 터뜨리기

n = int(input())
num = balloon = list(map(int, input().split(' ')))  # num은 위치확인
i = 0
result = []
while True:
    t = balloon[i]
    result.append(num[i])
    balloon.pop(i)
    if t > 0:
        i += t
        if i > n:
            i = n - t
    else:
        i += t
        if i < 0:
            i += n
    if len(balloon) == 0:
        break

print(*result, end=" ")
