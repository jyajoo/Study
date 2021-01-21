#한수

n = int(input())
cnt = 0
if n<=99:
    cnt = n

else:
    cnt += 99
    for i in range(100, n+1):
        i = list(map(int, str(i)))
        if i[0]-i[1] == i[1] - i[2]:
            cnt += 1

print(cnt)