#소수 찾기
#소수 : 자기 자신이랑 1이랑 약수를 지니고 있는 수 

n = int(input())
num = list(map(int, input().split()))

count = 0 #소수의 개수
def prime(n): #소수인지 아닌지
    cnt = 0
    if n == 1: #1은 소수가 아니다
        return False
    
    for i in range(2, n): #2부터 n-1까지 나눠보기
        if n%i == 0: #나머지가 0이면 소수가 아님
            cnt +=1
    if cnt ==0: #한 번도 나머지가 0이지 않았다면 소수!
        return True
    else:
        return False 

for i in num:
    if prime(i) == True:
        count += 1

print(count)