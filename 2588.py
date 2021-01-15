#곱셈
a = input()
b = input()

a = int(a)
b = int(b)

print("%d" %(a*(b%10)))
print("%d" %(a*((b%100)//10)))
print("%d" %(a*(b//100)))
print("%d" %(a*b))