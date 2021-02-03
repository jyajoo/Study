# 요세푸스 문제 0

from collections import deque
n, k = map(int, input().split(' '))

people = [i+1 for i in range(n)]
result = []
cnt = 0
while True:
    if cnt == len(people):
        cnt = 0
    for i in range(k):
        cnt += 1
        if cnt == len(people):
            cnt = 0
    cnt -= 1
    if cnt < 0:
        cnt = len(people)-1
    result.append(people[cnt])
    people.pop(cnt)
    if len(people) == 0:
        break

print("<", end="")
for i in range(len(result)):
    if i == len(result)-1:
        print(result[i], end="")
    else:
        print(result[i], end=", ")
print(">")
####################################################
# 요세푸스 문제 0_2 (덱으로 풀기)

n, k = map(int, input().split(' '))

deq = deque(i+1 for i in range(n))

print("<", end="")
while deq:  # 덱에 값이 있을 때 참
    for i in range(k-1):
        deq.append(deq.popleft())
    print(deq.popleft(), end="")
    if deq:
        print(", ", end="")
print(">")

# result = []
# while deq:
#     for i in range(k-1):
#         deq.append(deq.popleft())
#     result.append(deq.popleft())

# print("<" + ", ".join(map(str, result)) + ">")
