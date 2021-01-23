#분해합

n = int(input())
result = 0
for i in range(1, n+1):
    arr = list(map(int, str(i))) #분해합 구하기
    num = i + sum(arr)
    if num == n:
        result = i
        break
print(result)