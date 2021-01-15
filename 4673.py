#셀프 넘버

def d(n):
    sum = n
    num = list(str(n)) #만약 n이 13이면 ['1', '3']의 형태가 됨
    for i in num:
        sum += int(i)
    return sum
a = []
for i in range(10000):
    a.append(d(i+1))

for i in range(1, 10001):
    if i not in a:
        print(i)