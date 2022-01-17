X = int(input())

line = num = 1
while X > num: #주어진 수가 어느 줄에 해당하는 지(num은 해당 줄에서 가장 끝 수(큰 수))
    line += 1
    num += line

gap = num - X
if line % 2 == 0: #짝수 번째 줄일 경우
    a = line - gap
    b = gap + 1

else:
    a = gap + 1
    b = line - gap

print(f'{a}/{b}')