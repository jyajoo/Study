#ACM호텔
t = int(input())
for i in range(t):
    a = 0
    h, w, n = map(int, input().split())
    for k in range(w):
        for m in range(h):
            a += 1
            if a == n:
                print((m+1)*100+(k+1))