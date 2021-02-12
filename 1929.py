# 소수 구하기
# ? 시간 초과
m, n = map(int, input().split(' '))

arr = [i for i in range(m, n+1)]

for i in arr:
    if i == 1:
        continue
    if i == 2:
        print(i)
        continue
    cnt = 0
    for j in range(2, i):
        if i % j == 0:
            cnt += 1
    if cnt == 0:
        print(i)
###################################
# 소수 구하기_2 (에라토스테네스의 체)

def isprime(num):
    if num == 1:
        return False
    else: #else안에 안넣어줘도 됨.
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

m, n = map(int, input().split(' '))

for i in range(m, n+1):
    if isprime(i):
        print(i)
############################################
# 소수 구하기_3

def isprime(num):
    if num == 1:
        return False
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

m, n = map(int, input().split(' '))
for i in range(m, n+1):
    if isprime(i):
        print(i)
