# 프린터 큐

import sys

t = int(sys.stdin.readline().strip())
result = []
for _ in range(t):
    n, m = map(int, sys.stdin.readline().strip().split(' '))
    num = list(map(int, sys.stdin.readline().strip().split(' ')))  # 문서들의 중요도
    idx = [0 for _ in range(n)]
    idx[m] = "target"  # 몇 번째로 출력되는 지 궁금한 문서의 위치 표시
    cnt = 0  # 몇 번째로 출력되는 지

    while True:
        if num[0] == max(num):
            cnt += 1
            if idx[0] == "target":
                result.append(cnt)
                break
            else:
                del num[0]
                del idx[0]
        else:
            num.append(num[0])
            del num[0]
            idx.append(idx[0])
            del idx[0]
print(*result, sep="\n")
