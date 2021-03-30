import sys

def push(x):
    stack.append(x)

def pop():
    return -1 if not stack else stack.pop()

def size():
    return len(stack)

def empty():
    return 1 if not stack else 0

def top():
    return -1 if not stack else stack[-1]

n = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(n):
    tmp = sys.stdin.readline().split()
    op = tmp[0]

    if op == 'push':
        push(tmp[1])
    elif op == 'pop':
        print(pop())
    elif op == 'size':
        print(size())
    elif op == 'empty':
        print(empty())
    elif op == 'top':
        print(top())
