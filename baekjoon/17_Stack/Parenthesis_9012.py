import sys

t = int(sys.stdin.readline())

for _ in range(t):
    stack = []
    state = True
    tmp = list(sys.stdin.readline().rstrip())

    for val in tmp:
        if val == '(':
            stack.append(val)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                state = False
                break

    if state and not stack:
        print('YES')
    else:
        print('NO')