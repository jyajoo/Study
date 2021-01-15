#설탕 배달

n = num = int(input())

cnt = 0
num = num // 5 * 5 
while True:
    mod = n - num 
    if mod % 3 == 0:
        cnt += num//5 + mod//3
        break
    else:
        num -= 5
        if num <= 0:
            num = n
            if num % 3 == 0:
                cnt += num // 3
                break
            else:
                cnt = -1
                break
    
print(cnt)