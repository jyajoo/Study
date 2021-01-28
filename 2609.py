#최대공약수와 최소공배수

a, b = map(int, input().split(' '))
a_max = []
b_max = []
for i in range(1, a+1):
    if a % i == 0:
        a_max.append(i)
for i in range(1, b+1):
    if b % i == 0:
        b_max.append(i)

max_ = []
for i in a_max:
    if i in b_max:
        max_.append(i)
print(max(max_)) ### 최대공약수

i = 1
x = max(a, b)
y = min(a, b)
while True:
    z = x * i
    if z % y == 0:
        print(z)  ###최대공배수
        break
    i += 1
###########################################
#최대공약수와 최소공배수_2

a, b = map(int, input().split(' '))
x, y = a, b
while b != 0:
    r = a%b
    a, b = b, r
print(a)
print(x*y//a)