#직각삼각형

while True:
    a = list(map(int, input().split(' ')))
    if a == [0, 0, 0]:
        break
    a.sort()
    # if sum(a) == 0:
    #     break
    # max_num = max(a)
    # a.remove(max_num)
    if a[2]**2 == a[0]**2 + a[1]**2:
        print("right")
    else:
        print("wrong")