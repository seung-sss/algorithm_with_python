import sys

while True:
    tmp = sys.stdin.readline().rstrip()
    if tmp == '.':
        break

    stack = []
    state = True

    for val in list(tmp):
        if val == '(' or val == '[':
            stack.append(val)
        elif val == ')':
            if not stack or stack[-1] == '[':
                state = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif val == ']':
            if not stack or stack[-1] == '(':
                state = False
                break
            elif stack[-1] == '[':
                stack.pop()

    if state and not stack:
        print('yes')
    else:
        print('no')