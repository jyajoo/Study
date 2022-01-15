#국영수

n = int(input())
arr = []
for i in range(n):
    a, b, c, d = input().split()
    arr.append((a, int(b), int(c), int(d)))

arr.sort(key = lambda x : (-x[1], x[2], -x[3], x[0])) #-는 내림차순

for i in arr:
    print(i[0])