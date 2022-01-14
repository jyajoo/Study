#수 찾기
#! 시간복잡도 O(N)
#? 시간초과!
n = int(input())
a = list(map(int, input().split(' ')))
m = int(input())
b = list(map(int, input().split(' ')))
result = []
for i in b:
    if i in a:
        result.append(1)
    else:
        result.append(0)
print(*result, sep = "\n")
##############################################
#수 찾기_2
#! 시간 복잡도 O(logN)
#? 이분 탐색
n = int(input())
a = list(map(int, input().split(' ')))
a.sort()
m = int(input())
b = list(map(int, input().split(' ')))
result = []

for i in b:
    left = 0
    right = n - 1
    while(left<=right):
        mid = (left+right)//2
        if i < a[mid]:
            right = mid -1
        elif i > a[mid]:
            left = mid + 1
        elif i == a[mid]:
            result.append(1)
            break
    if left > right:
        result.append(0)
print(*result, sep = "\n")
##############################################
#수 찾기_3
#! set, dictionary의 시간 복잡도는 O(1)
n = int(input())
a = set(map(int, input().split(' ')))
m = int(input())
b = list(map(int, input().split(' ')))
result = []
for i in b:
    if i in a:
        print(1, sep = "\n")
    else:
        print(0, sep = "\n")