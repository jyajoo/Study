# 더하기 사이클

n = int(input())
if n < 10:
    n = n * 10
count = 0

a = n // 10
b = n % 10

while True:
    sum = a + b
    if sum >= 10:
        sum = sum % 10
    sum = b*10 + sum
    count += 1
    if sum == n:
        break
    a = sum//10
    b = sum % 10

print(count)

#################################################
# 더하기 사이클_2
n = check = int(input())

if n < 10:
    n = n * 10
count = 0

while True:
    ten = n//10
    one = n % 10
    sum = ten + one
    count += 1
    n = int(str(one)+str(sum % 10))
    if n == check:
        break
print(count)

##################################################
# 더하기 사이클_3
n = check = int(input())

if n < 10:
    n = n * 10
count = 0
while True:
    tmp = n//10 + n % 10
    sum = (n % 10)*10 + tmp % 10
    count += 1
    n = sum
    if sum == check:
        break
print(count)

#################################################
# 더하기 사이클_4 (문자열)
n = a = input()
cnt = 0
if(int(a) < 10):
    a = "0" + a

while(True):
    cnt += 1
    b = str(int(a[0]) + int(a[1]))
    if(int(b) >= 10):
        b = b[1]
    a = a[1] + b
    if(int(a) == int(n)):
        print(cnt)
        break
