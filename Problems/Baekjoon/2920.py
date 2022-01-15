#음계

asc = [1, 2, 3, 4, 5, 6, 7, 8]
des = [8, 7, 6, 5, 4, 3, 2, 1]

num = list(map(int, input().split()))

count1 = count2 = 0
for j in range(8):
    if asc[j] == num[j]:
        count1 += 1
    elif des[j] == num[j]:
        count2 += 1
    
if count1 == 8:
    print("ascending")
elif count2 == 8:
    print("descending")
else:
    print("mixed")