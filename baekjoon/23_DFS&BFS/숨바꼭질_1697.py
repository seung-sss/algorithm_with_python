# 시간초과됨
import sys
from collections import deque

def bfs(n, k):
    queue = deque([n])
    move = [-1, 1, 2]

    while queue:
        now = queue.popleft()
        if now == k:
            return loc[now]

        for i in range(3):
            if move[i] == 2:
                new = now * move[i]
            else:
                new = now + move[i]

            if check(new):
                loc[new] = loc[now] + 1
                queue.append(new)

def check(new):
    if 0 <= new < len(loc) and loc[new] == None:
        return True
    else:
        return False

n, k = map(int, sys.stdin.readline().split())
loc = [None] * 100000
loc[n] = 0 # 시작점

print(bfs(n, k))



