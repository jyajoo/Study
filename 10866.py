# 덱
import sys
from collections import deque

deq = deque()
result = []
n = int(sys.stdin.readline())
for _ in range(n):
    cmd_input = sys.stdin.readline().strip().split(' ')
    cmd = cmd_input[0]
    if cmd == "push_front":
        deq.appendleft(int(cmd_input[1]))
    elif cmd == "push_back":
        deq.append(int(cmd_input[1]))
    elif cmd == "pop_front":
        if len(deq) != 0:
            result.append(deq.popleft())
        else:
            result.append(-1)
    elif cmd == "pop_back":
        if len(deq) != 0:
            result.append(deq.pop())
        else:
            result.append(-1)
    elif cmd == "size":
        result.append(len(deq))
    elif cmd == "empty":
        if len(deq) == 0:
            result.append(1)
        else:
            result.append(0)
    elif cmd == "front":
        if len(deq) != 0:
            # n = deq.popleft()
            # result.append(n)
            # deq.appendleft(n)
            result.append(deq[0])
        else:
            result.append(-1)
    elif cmd == "back":
        if len(deq) != 0:
            # n = deq.pop()
            # result.append(n)
            # deq.append(n)
            result.append(deq[len(deq)-1])
        else:
            result.append(-1)
print(*result, sep="\n")
