# 평균은 넘겠지
c = int(input())

for i in range(c):
    stu = list(map(int, input().split(' ')))

    sum = 0
    count = 0
    for j in range(len(stu)-1):
        sum += stu[j+1]

    avg = sum/(stu[0])

    for k in range(len(stu)-1):
        if avg < stu[k+1]:
            count += 1
    result = count / stu[0] * 100
    print("%.3f%%" % result)

###############################################
# 평균은 넘겠지_2
n = int(input())

for _ in range(n):  # 언더스코어
    stu = list(map(int, input().split(' ')))
    avg = sum(stu[1:])/stu[0]  # sum함수를 이용해서 리스트 1부터 끝까지 모두 합쳐준다.
    count = 0
    for i in stu[1:]:
        if i > avg:
            count += 1
    result = count / stu[0] * 100
    print("%.3f%%" % result)

###############################################
# 평균은 넘겠지_3

c = int(input())
for i in range(c):
    score = list(map(int, input().split(' ')))
    avg = ratio = 0
    for j in range(1, score[0] + 1):
        avg += score[j]
    avg = avg / score[0]
    for j in range(1, score[0] + 1):
        if score[j] > avg:
            ratio += 1
    ratio = round((ratio / score[0]) * 100, 3)
    print("{:.3f}".format(ratio) + "%")
