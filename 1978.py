#소수 찾기
n = int(input())

m = list(map(int, input().split()))

count = 0 #소수의 개수

for i in m:
    cnt = 0
    if i == 1: #소수가 아님
        continue #아래 코드를 실행하지 않고 건너뜀!!! #?또는 cnt +=1을 해준다.
    
    for j in range(2, i): #2부터 i-1까지 차례대로 나누기
        if i%j == 0: #나머지가 0이면 소수가 아님!
            cnt += 1
    if cnt == 0: #나머지가 한 번도 0이 아닐 경우엔 소수
        count += 1

print(count)
