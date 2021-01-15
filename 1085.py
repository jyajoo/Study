#직사각형에서 탈출

x, y, w, h = list(map(int, input().split()))

if x >= 1 and x <= w-1 and y >=1 and y <= h-1:
        #w-x, h-y, x, y 중 가장 작은 값이 최소 거리
        lis = [w-x, h-y, x, y]

        print(min(lis))