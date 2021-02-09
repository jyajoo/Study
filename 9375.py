# 패션왕 신해빈
from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        clothes, kind = input().split(' ')
        arr.append(kind)
    wear = Counter(arr)
    result = 1
    for i in wear.values():
        result *= i + 1
    print(result-1)
