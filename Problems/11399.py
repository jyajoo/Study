#ATM

n = int(input())

person = list(map(int, input().split(' ')))
person.sort()
time = result = 0
for i in person:
    time += i
    result += time
print(result)