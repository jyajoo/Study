# 숫자의 개수

a = int(input())
b = int(input())
c = int(input())

mul = str(a * b * c)

num = [i*0 for i in range(10)]
for i in mul:
    num[int(i)] += 1

for i in num:
    print(i)

#####################################
# 숫자의 개수_2

a = int(input())
b = int(input())
c = int(input())

mul = str(a*b*c)

for i in range(10):
    print(mul.count(str(i)))

#####################################
# 숫자의 개수_3

a = int(input())
b = int(input())
c = int(input())

result = str(a * b * c)

for i in range(0, 10):
    cnt = 0
    for j in result:
        if(int(j) == i):
            cnt += 1
    print(cnt)
