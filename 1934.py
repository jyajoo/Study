#최소공배수

t = int(input())
for _ in range(t):
    x, y = map(int, input().split(' '))
    a, b = x, y
    while b!=0:
        r = a % b
        a, b = b, r #유클리드 호제법
    print(int(x * y / a))