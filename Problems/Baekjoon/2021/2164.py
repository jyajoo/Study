#카드 2
#? 시간 초과 아무래도 덱을 사용해야 하나 보다.
from queue import Queue

n = int(input())
que = Queue()
for i in range(n):
    que.put(i+1)

while (que.qsize()>1):
    que.get()
    que.put(que.get())

print(que.get())
##################################
#카드 2_2
from collections import deque

n = int(input())
deq = deque()
for i in range(n):
    deq.append(i+1)

while (len(deq)>1):
    deq.popleft()
    deq.append(deq.popleft())

print(deq.pop())