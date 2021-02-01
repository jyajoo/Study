# 숫자 카드 2 (시간 초과)
from collections import Counter
import sys
n = int(sys.stdin.readline())
arr1 = list(map(int, input().split(' ')))

m = int(sys.stdin.readline())
arr2 = list(map(int, input().split(' ')))
result = []
for i in arr2:
    result.append(arr1.count(i))

print(*result, end=" ")

##############################################
# 숫자 카드 2_2 (해시 테이블로 시간 초과 해결)

n = int(sys.stdin.readline().strip())
arr1 = list(map(int, sys.stdin.readline().split(' ')))
arr1 = Counter(arr1)

m = int(sys.stdin.readline().strip())
arr2 = list(map(int, sys.stdin.readline().split(' ')))

for i in arr2:
    print(arr1[i], end=" ")

# for i in arr2:
#     if i in arr1:
#         print(arr1[i], end=" ")
#     else:
#         print(0, end=" ")
# ? print(' '.join(f'{arr1[i]}' if i in arr2 else 0 for i in arr2))
