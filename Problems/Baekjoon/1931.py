#회의실 배정

n = int(input()) #회의의 수
meeting = []
for _ in range(n): 
    x, y = map(int, input().split(' '))
    meeting.append((x, y))

meeting.sort(key = lambda x : (x[0], x[1]))

# cnt = 1
# end = meeting[0][1]
# for i in range(1, n):
#     if end > meeting[i][0]:
#         pass
#     else:
#         end = meeting[i][1]
#         cnt += 1
# print(cnt)
cnt = end = 0
for i, j in meeting:
    if i >= end:
        cnt += 1
        end = j
print(cnt)