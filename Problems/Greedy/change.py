n = int(input())   # 거슬러 줘야 할 돈
coin = [500, 100, 50, 10]   # 거스름돈으로 사용되는 동전

result = 0   # 최소 개수

for i in coin:   # 거스름돈 단위가 큰 것부터
    result += n // i   # 몫
    n %= i   # 나머지

print(result)
