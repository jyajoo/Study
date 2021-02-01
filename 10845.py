# 큐
import sys
queue = []
result = []
n = int(sys.stdin.readline())
for _ in range(n):
    cmd_input = sys.stdin.readline().strip().split(' ')
    cmd = cmd_input[0]
    if cmd == "push":
        queue.append(int(cmd_input[1]))
    elif cmd == "pop":
        if len(queue) != 0:
            result.append(queue[0])
            queue.remove(queue[0])
        else:
            result.append(-1)
    elif cmd == "size":
        result.append(len(queue))
    elif cmd == "empty":
        if len(queue) == 0:
            result.append(1)
        else:
            result.append(0)
    elif cmd == "front":
        if len(queue) != 0:
            result.append(queue[0])
        else:
            result.append(-1)
    elif cmd == "back":
        if len(queue) != 0:
            result.append(queue[len(queue)-1])
        else:
            result.append(-1)
print(*result, sep="\n")
