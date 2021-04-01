import sys
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        tmp = queue.popleft()
        a, b = tmp[0], tmp[1]

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx, ny])

    return

t = int(sys.stdin.readline())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0]*m for i in range(n)]
    # loc = []
    # 배추가 있는 곳은 1로 표시
    for i in range(k):
        y, x = map(int, sys.stdin.readline().split())
        graph[x][y] = 1
        # loc.append((x, y))

    res = 0
    # for val in loc:
    #     if graph[val[0]][val[1]] == 1:
    #         bfs(val[0], val[1])
    #         res += 1

    # 결과에서 그냥 이중 for문 돌리는게 시간적으로 조금 더 빨랐음
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                res += 1

    print(res)

