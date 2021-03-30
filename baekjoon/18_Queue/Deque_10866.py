import sys
from collections import deque

n = int(sys.stdin.readline())
dq = deque([])
for _ in range(n):
    inp = sys.stdin.readline().split()

    if inp[0] == 'push_front':
        dq.appendleft(inp[1])
    elif inp[0] == 'push_back':
        dq.append(inp[1])
    elif inp[0] == 'pop_front':
        print(-1) if not dq else print(dq.popleft())
    elif inp[0] == 'pop_back':
        print(-1) if not dq else print(dq.pop())
    elif inp[0] == 'size':
        print(len(dq))
    elif inp[0] == 'empty':
        print(1) if not dq else print(0)
    elif inp[0] == 'front':
        print(-1) if not dq else print(dq[0])
    elif inp[0] == 'back':
        print(-1) if not dq else print(dq[-1])