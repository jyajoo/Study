#나이순 정렬

n = int(input())
person = []
for _ in range(n):
    age, name = input().split(' ')
    person.append([int(age),name])
person.sort(key=lambda x : (x[0]))

for i in person:
    print(i[0], i[1])