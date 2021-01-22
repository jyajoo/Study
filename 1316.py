#그룹 단어 체커

n = int(input())
cnt = 0
for _ in range(n):
    s = list(input())
    arr = []
    no = 0
    for i in range(len(s)):
        if s[i] in arr:
            if s[i-1] != s[i]:
                no += 1
                break
        else:
            arr.append(s[i])
    if no ==0:
        cnt += 1
print(cnt)