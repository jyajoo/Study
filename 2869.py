#달팽이는 올라가고 싶다

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

#달팽이는 올라가고 싶다_2

a, b, v = map(int, input().split(' '))

day = (v-a)/(a-b)

if day == int(day):
    day = int(day)
else:
    day = int(day) + 1

print(day+1)