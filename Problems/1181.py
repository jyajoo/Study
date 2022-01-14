#단어 정렬

n = int(input())
arr = []

for _ in range(n):
    arr.append(input())

arr = list(set(arr)) #set으로 중복 제거, sort이용을 위해 다시 리스트 형으로
arr.sort(key = lambda x : (len(x), x)) #그냥 sort()를 해주면, 사전 순으로 정렬
print(*arr, sep = "\n")