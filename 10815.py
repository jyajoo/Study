# 숫자 카드 (시간초과)

n = int(input())
arr = list(map(int, input().split(' ')))

m = int(input())
arr2 = list(map(int, input().split(' ')))

for i in range(m):
    if arr2[i] in arr:
        arr2[i] = 1
    else:
        arr2[i] = 0

print(*arr2, end="")

################################################
# 숫자카드_2 (이분 탐색으로 시간 초과 해결)

n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()
m = int(input())
arr2 = list(map(int, input().split(' ')))

result = []
for i in arr2:
    left = 0
    right = n-1
    while (left <= right):
        mid = (left+right)//2
        if i < arr[mid]:
            right = mid - 1
        elif i > arr[mid]:
            left = mid + 1
        elif i == arr[mid]:
            result.append(1)
            break
    if left > right:
        result.append(0)

print(*result, end="")
