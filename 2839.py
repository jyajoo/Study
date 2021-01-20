# #설탕 배달

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
##############################################
#설탕 배달_2

n = int(input())
cnt = 0
while True:
    if n % 5 == 0:
        cnt += n//5
        break
    else:
        n = n-3
        if n<0:
            cnt = -1
            break
        cnt += 1
print(cnt)