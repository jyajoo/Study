n = check = int(input())

if n < 10:
    n = n * 10
count = 0
"""
while True:
    ten = n//10
    one = n % 10
    sum = ten + one
    count += 1
    n = int(str(n % 10)+str(sum % 10))
    if n == check:
        break
print(count)
"""
while True:
    tmp = n//10 + n%10
    sum = (n%10)*10 + tmp%10
    count += 1
    n = sum
    if sum == check:
        break
print(count)