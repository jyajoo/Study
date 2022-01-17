#손익분기점

a, b, c = map(int, input().split(' '))
point = 1

while True:
    if b >= c:
        point = -1
        break
    cost = a + point * b
    money = c * point
    if cost < money:
        break
    point += 1

print(point)  # 시간 초과

#############################################
#손익분기점_2

a, b, c = map(int, input().split(' '))

if b >= c:
    print(-1)

else:
    print(int(a/(c-b)+1))