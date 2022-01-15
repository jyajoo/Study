# 제로

k = int(input())
num = []

for _ in range(k):
    a = int(input())
    if a != 0:
        num.append(a)
    else:
        if len(num) != 0:
            num.pop()
result = 0
for i in num:
    result += i

print(result)
