#수리공 항승

import sys
n, l = map(int, sys.stdin.readline().split(' '))
water = list(map(int, sys.stdin.readline().split(' ')))
water.sort()
cnt = 0
start = 0
for i in water:
    if i > start:
        start = i + l -1
        cnt += 1
print(cnt)