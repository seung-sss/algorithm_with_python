import sys
from collections import deque

n = int(sys.stdin.readline())
que = deque([])

for _ in range(n):
    inp = sys.stdin.readline().split()
    ins = inp[0]

    if ins == 'push':
        que.append(int(inp[1]))
    elif ins == 'pop':
        print(-1) if not que else print(que.popleft())
    elif ins == 'size':
        print(len(que))
    elif ins == 'empty':
        print(1) if not que else print(0)
    elif ins == 'front':
        print(-1) if not que else print(que[0])
    elif ins == 'back':
        print(-1) if not que else print(que[-1])