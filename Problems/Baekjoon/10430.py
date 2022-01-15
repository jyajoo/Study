#나머지
a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

print("%d" %((a+b)%c))
print("%d" %(((a%c)+(b%c))%c))
print("%d" %((a*b)%c))
print("%d" %(((a%c) * (b%c))%c))