t = int(input()) #테스트 케이스의 개수

for i in range(t):
    r, s = input().split() #r : 반복횟수, s : 문자열 / split() : 공백을 구분하여 값을 받는다.
    temp = ""
    for j in s:
        temp += int(r)*j
    print(temp)