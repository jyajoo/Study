#캠핑

import sys
cnt = 1
while True:
    day = 0
    l, p, v = map(int, sys.stdin.readline().split(' '))

    if l ==0 and p ==0 and v ==0:
        break

    day += l * (v//p) + min(v%p, l) 

    print("Case %d: %d" %(cnt, day))
    cnt += 1 



k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]
start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2 
    lines = 0 
    for i in lan:
        lines += i // mid 
        
    if lines >= n: 
        start = mid + 1
    else:
        end = mid - 1
print(end)


n = int(input())
student = []

for _ in range(n):
    weight, height = map(int, input().split())
    student.append((weight, height))

for i in student:
    rank = 1
    for j in student:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")4


n = int(input())
t = []
p = []
dp = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)
for i in range(n - 1, -1, -1):
    if t[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
print(dp[0])



n, m = map(int, input().split())
visited = [False] * n  
result = []  

def solve(depth, n, m):
    if depth == m:  
        print(' '.join(map(str, result))) 
        return
    for i in range(len(visited)):  
        if not visited[i]: 
            visited[i] = True 
            result.append(i+1)
            solve(depth+1, n, m) 
            visited[i] = False 
            result.pop()  

solve(0, n, m)