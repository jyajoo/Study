#상수

a, b = input().split(' ')

a = list(a)
b = list(b)

a.reverse()
b.reverse()

num1 = num2 = ""

for i in a:
    num1 += i
for i in b:
    num2 += i

num1 = int(num1)
num2 = int(num2)

print(max(num1, num2))

#################################################
#상수_2
a, b = input().split(' ')

num1 = int("".join(i for i in a[::-1]))
num2 = int("".join(i for i in b[::-1]))

print(max(num1, num2))