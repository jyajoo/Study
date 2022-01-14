#OX퀴즈
a = input() #테스트 케이스의 개수

for i in range(int(a)): 
    test = list(input()) #OOXO와 같은 문자열을 입력받아 ['O','O','X','O']형태로 변환
    score = 0
    result = 0
    for j in test:
        if j == "O":
            score += 1
            result += score
        elif j == "X":
            score = 0
    print(result)        