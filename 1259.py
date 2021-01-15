#팰린드롬수
while True:
    n = input()

    if n == '0':
        break
    
    if n[::-1] == n: #a:b:c a부터 b까지 c의 간격인 배열
        print("yes")
    else:
        print("no")