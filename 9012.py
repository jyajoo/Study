#괄호

t = int(input())
result = []
for _ in range(t):
    vps = list(input())
    cnt = 0
    for i in vps:
        if i == "(":
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                break
    if cnt == 0:
        result.append("YES")
    else:
        result.append("NO")
print(*result, sep="\n")