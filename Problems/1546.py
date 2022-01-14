#평균
n = int(input())

score = list(map(int, input().split()))
M = max(score)
sum = 0
for i in range(len(score)):
    score[i] = score[i]/M*100
    sum += score[i]

print(sum/len(score))