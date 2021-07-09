# 벌집

n = int(input())

i = 1
x = 2
y = 8
while True:
    if n == 1:
        cnt = 1
        break
    if n in range(x, y):
        cnt = i + 1
        break
    i += 1
    x = y
    y = (6 * i) + x

print(cnt)

######################################
# 벌집_2

n = int(input())

x = 1
y = 1
cnt = 1
while n > y:
    y += cnt*6
    cnt += 1

print(cnt)
######################################
# 벌집_3
a = int(input())
cnt = 0
room = 1
while True:
    cnt += 1
    if room >= a:
        print(cnt)
        break
    room += 6 * cnt
