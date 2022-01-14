# 나머지
num = []
for i in range(10):
    num.append(int(input()))
    num[i] = num[i] % 42

num = set(num)  # set() : 집합 함수 , 중복을 허용하지 않는다, 순서가 없다.

print(len(num))

##########################################################
# 나머지_2
a = {}  # dictionary 자료형 : key는 변할 수 없다. value는 상관없

for i in range(10):
    b = int(input())
    a[b % 42] = i

print(len(a))
##########################################################
# 나머지_3
num = []
result = []
for i in range(10):
    x = int(input()) % 42
    num.append(x)
    if(x not in result):
        result.append(x)

print(len(result))
