# pypy3 제출 시 속도 약 3.5배 빨랐음
import sys
from collections import deque

def bfs(m, n, box):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    days = -1
    queue = deque()

    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                queue.append([i, j])

    while queue:
        days += 1

        for _ in range(len(queue)):
            a, b = queue.popleft()

            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]

                if (0 <= nx < n) and (0 <= ny < m) and (box[nx][ny] == 0):
                    box[nx][ny] = box[a][b] + 1
                    queue.append([nx, ny])

    for b in box:
        if 0 in b:
            return -1

    return days


m, n = map(int, sys.stdin.readline().split())
box = []

for _ in range(n):
    box.append(list(map(int, sys.stdin.readline().split())))

print(bfs(m, n, box))

