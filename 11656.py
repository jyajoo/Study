#접미사 배열

S = input()

arr = []
for i in range(len(S)):
    arr.append(S[i:])

arr.sort()
print(*arr, sep = "\n")