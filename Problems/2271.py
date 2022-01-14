#로프

n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))

rope.sort()
rope.reverse()
#rope.sort(reverse = True) 최대 중량을 버틸수 있는 로프 순으로

m = 0
for i in range(n):
    if m < rope[i] * (i+1): #최대 중량 x 해당 개수들 중 최대 중량
        m = rope[i] * (i+1)
print(m)
