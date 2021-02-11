#파도반 수열

t = int(input())
for _ in range(t):
    num = int(input())
    arr = [1, 1, 1, 2, 2]
    if num > 4:
        for i in range(5, num):
            arr.append(arr[i-1]+arr[i-5])
    print(arr[num-1])