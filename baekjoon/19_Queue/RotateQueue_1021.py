import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
target = list(map(int, sys.stdin.readline().split()))
dq = deque([i for i in range(n)])

cnt = 0

for i in range(m):
    idx = dq.index(target[i]-1)
    if idx <= len(dq) - idx:
        for j in range(idx):
            dq.append(dq.popleft())
            cnt += 1
    else:
        for j in range(len(dq) - idx):
            dq.appendleft(dq.pop())
            cnt += 1

    dq.popleft()

print(cnt)


