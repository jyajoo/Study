# 회전하는 큐(둘 다 연산하고 최소값으로 구해주기)

from collections import deque
n, m = map(int, input().split(' '))  # n : 큐의 크기, m : 몇 번 뽑아낼 건지
arr = list(map(int, input().split(' ')))  # m번동안 어느 위치를 뽑아낼 건지

num2 = [i+1 for i in range(n)]  # 두 번째 연산을 할 큐
num3 = [i+1 for i in range(n)]  # 세 번째 연산을 할 큐
result = 0  # 연산의 최솟값(결과)

for i in arr:
    cnt2 = cnt3 = 0
    while True:  # 123 -> 231
        if num2[0] == i:
            num2.pop(0)
            break
        num2.append(num2.pop(0))
        cnt2 += 1
    while True:  # 123 -> 312
        if num3[0] == i:
            num3.pop(0)
            break
        num3.insert(0, num3.pop())
        cnt3 += 1
    result += min(cnt2, cnt3)

print(result)
########################################
# 회전하는 큐_2(어느 방식이 최소인지 먼저 판단)


def cnt2(que):  # 123 -> 231
    global cnt
    que.append(que.pop(0))
    cnt += 1


def cnt3(que):  # 123 -> 312
    global cnt
    que.insert(0, que.pop())
    cnt += 1


n, m = map(int, input().split(' '))  # n : 큐의 크기, m : 몇 번 뽑아낼 건지
arr = list(map(int, input().split(' ')))

num = [i for i in range(1, n+1)]  # 큐
cnt = 0

while arr:
    if num[0] == arr[0]:
        num.pop(0)
        arr.pop(0)
    else:
        if num.index(arr[0]) <= len(num)//2:  # 뽑아내려는 값의 위치가 큐의 반보다 작은 경우
            while num[0] != arr[0]:
                cnt2(num)
        else:
            while num[0] != arr[0]:
                cnt3(num)

print(cnt)
#########################################################################################
# 회전하는 큐_3(덱에서 rotate함수 이용)


n, m = map(int, input().split(' '))  # n : 큐의 크기, m : 몇 번 뽑아낼 건지
arr = list(map(int, input().split(' ')))

que = deque(range(1, n+1))

cnt = 0

for i in arr:
    if i == que[0]:
        que.popleft()
        continue

    q_idx = que.index(i)

    if q_idx <= len(que)//2:
        que.rotate(-q_idx)
        cnt += q_idx

    else:
        que.rotate(len(que)-q_idx)
        cnt += len(que)-q_idx

    que.popleft()
print(cnt)
