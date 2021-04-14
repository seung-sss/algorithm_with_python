import sys
from collections import deque

def bfs(m, n, h, box):
    dz = [0, 0, 0, 0, -1, 1]
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]

    days = -1

    while queue:
        days += 1

        for _ in range(len(queue)):
            z, x, y = queue.popleft()

            for i in range(6):
                nz = z + dz[i]
                nx = x + dx[i]
                ny = y + dy[i]

                if (0 <= nz < h) and (0 <= nx < n) and (0 <= ny < m) and (box[nz][nx][ny] == 0):
                    box[nz][nx][ny] = box[z][x][y] + 1
                    queue.append([nz, nx, ny])

    # for b in box:
    #     for bb in b:
    #         if 0 in bb:
    #             return -1
    #
    # return days

    if check(box):
        return days
    else:
        return -1

def check(box): # 시간차 없음
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 0:
                    return False
                    break

    return True

m, n, h = map(int, sys.stdin.readline().split())
box, queue = [], deque()

for i in range(h):
    tmp = []
    for j in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        for k in range(m):
            if row[k] == 1:
                queue.append([i, j, k])
        tmp.append(row)
    box.append(tmp)

print(bfs(m, n, h, box))