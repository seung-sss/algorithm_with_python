import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    p = deque(list(sys.stdin.readline().rstrip()))
    n = int(sys.stdin.readline())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    check = True

    while p:
        if len(p) >= 2 and p[0] == 'R' and p[1] == 'R':
            p.popleft()
            p.popleft()

        if p[0] == 'R':
            arr.reverse()

        elif p[0] == 'D':
            if not arr:
                check = False
                break
            arr.popleft()

        p.popleft()

    if check:
        print('[', end = '')
        for i in range(len(arr) - 1):
            print(arr[i] + ',', end = '')
        print(arr[-1] + ']')
    else:
        print('error')