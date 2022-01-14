#알람 시계

a, b = map(int, input().split())

if b >= 45:
    b = b - 45

else:
    b = b + 15
    a = a - 1
    if a < 0:
        a = 24 + a

print("%d %d" %(a, b))