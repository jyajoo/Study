#문자열 집합

import sys
a = sys.stdin.readline

n, m = map(int, a().split(' '))
string = {a().strip(' ') for _ in range(n)}
cnt = 0

for j in range(m):
    str = a().strip()
    if str in string:
        cnt += 1

print(cnt)