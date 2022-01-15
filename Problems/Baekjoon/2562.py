#최댓값
num = []
for i in range(9): #0 ~ 8
    a = input() #입력 받기
    number = int(a)
    num.append(number) #리스트에 추가해주기

max = 0
max_number = 0
for j in range(9):
    if max < num[j]:
        max = num[j]
        max_number = j

print(max)
print(max_number)

#############################################
#최댓값_2

num = []
for i in range(9):
    a = int(input())
    num.append(a)

print(max(num))
print(num.index(max(num))+1)