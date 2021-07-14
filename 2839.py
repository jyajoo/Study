# 설탕 배달

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
# 설탕 배달_2 [그리디]

n = int(input())
cnt = 0
while True:
    if n % 5 == 0:
        cnt += n//5
        break
    else:
        n = n-3
        if n < 0:
            cnt = -1
            break
        cnt += 1
print(cnt)

##############################################
# 설탕 배달_3[다이나믹]


def dynamic(n):
    if n < 3 or n == 4 or n == 7:
        return dp[n]

    elif n == 3 or n == 5:
        dp[n] = 1
        return dp[n]

    if dynamic(n-3) < 0 or dynamic(n-5) < 0:
        return 1 + max(dynamic(n-3), dynamic(n-5))

    return 1 + min(dynamic(n-3), dynamic(n-5))


x = int(input())
dp = [-1] * (x + 1)
print(dynamic(x))

##############################################
# 설탕 배달_4

x = int(input())
dp = [-1] * (x + 1)

if x >= 3:
    dp[3] = 1
if x >= 5:
    dp[5] = 1

for i in range(6, x + 1):
    if dp[i - 3] < 0 and dp[i - 5] < 0:
        dp[i] = -1

    elif dp[i - 3] > 0 and dp[i - 5] > 0:
        dp[i] = 1 + min(dp[i - 3], dp[i - 5])

    else:
        dp[i] = 1 + max(dp[i - 3], dp[i - 5])

print(dp[x])
