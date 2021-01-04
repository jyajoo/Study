a = input() #테스트 케이스의 개수


for i in range(int(a)):
    test = list(input())
    score = 0
    result = 0
    for j in test:
        if j == "O":
            score += 1
            result += score
        elif j == "X":
            score = 0
    print(result)        