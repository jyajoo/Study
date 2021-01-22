#피보나치 수 5

n = int(input())
a = 0
b = 1
c = 0
for _ in range(n-1):
    c = a + b
    a = b
    b = c
if n == 0:
    b = 0
print(b)
##################################
#피보나치 수 5_2 (재귀로 풀기)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))