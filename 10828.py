#스택
import sys
n = int(sys.stdin.readline())
stack = []
result = []
for _ in range(n):
    cmd_input = sys.stdin.readline().strip().split(' ')
    cmd = cmd_input[0]
    if cmd == "push":
        stack.append(int(cmd_input[1]))
    elif cmd == "pop":
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack.pop())
    elif cmd == "size":
        result.append(len(stack))
    elif cmd == "empty":
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)
    elif cmd == "top":
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[len(stack)-1])
print(*result, sep = "\n")