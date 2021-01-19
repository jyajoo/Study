# #달팽이는 올라가고 싶다

# a, b, v = map(int, input().split(' '))

# cnt = meter = 0

# while True:
#     meter += a
#     if meter >= v:
#         cnt += 1
#         break
#     meter -= b
#     cnt += 1

# print(cnt)

#달팽이는 올라가고 싶다

a, b, v = map(int, input().split(' '))

cnt = meter = 0

while True:
    i = v // a
    if i == 0 or v%a==0:
        cnt += 1
        break
    gap = (a-b) * i
    v -= gap
    cnt += i
    if v<=0:
        break

print(cnt)