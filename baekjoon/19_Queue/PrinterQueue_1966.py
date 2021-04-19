import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    que = deque(list(map(int, sys.stdin.readline().split())))
    idx = deque([i for i in range(n)])

    order = 0
    while True:
        if que[0] == max(que):
            order += 1

            if idx[0] == m:
                print(order)
                break
            else:
                que.popleft()
                idx.popleft()

        else:
            que.append(que.popleft())
            idx.append(idx.popleft())

