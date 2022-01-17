# 1로 만들기 (bottom-up)

N = int(input())

dp = [0 for _ in range(N+1)]  # N만큼의 리스트 생성

for i in range(2, N+1):  # 2부터 N까지 반복
    dp[i] = dp[i-1] + 1  # 3번 연산
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:  # 3번보다 2번이 더 작은 경우
        dp[i] = dp[i//2] + 1
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:  # 3번보다 1번이 더 작은 경우
        dp[i] = dp[i//3] + 1

print(dp[N])
