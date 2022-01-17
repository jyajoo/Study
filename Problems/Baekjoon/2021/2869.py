# 달팽이는 올라가고 싶다

a, b, v = map(int, input().split(' '))

cnt = meter = 0

while True:
    meter += a
    if meter >= v:
        cnt += 1
        break
    meter -= b
    cnt += 1

print(cnt)

#######################################
# 달팽이는 올라가고 싶다_2

a, b, v = map(int, input().split(' '))

day = (v-a)/(a-b)

if day == int(day):
    day = int(day)
else:
    day = int(day) + 1

print(day+1)

#######################################
# 달팽이는 올라가고 싶다_3
# import math
a, b, v = map(int, input().split())  # a : 올라감, b : 미끄러짐, v : 총 길이

print(math.ceil((v - b) / (a - b)))
