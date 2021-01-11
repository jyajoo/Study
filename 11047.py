#동전 0
n, k = map(int, input().split(' '))
coin = []
for i in range(n):
    coin.append(int(input())) #오름차순으로 동전 n개 받기
coin = coin[::-1]
a = 0
for i in range(len(coin)): #가장 큰 돈부터 작은 돈까지
    if coin[i] <= k: #k보다 작아야함
        a += k//coin[i] #동전 개수
        b = k%coin[i] #남은 돈
        k = b
        if k == 0:
            break
print(a)