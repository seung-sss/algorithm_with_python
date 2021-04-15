import sys
from collections import deque

def bfs():
    sx, sy = map(int, sys.stdin.readline().split())
    ex, ey = map(int, sys.stdin.readline().split())

    queue = deque()
    queue.append([sx, sy])

    while queue:
        x, y = queue.popleft()

        if x == ex and y == ey:
            return graph[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue

            if not graph[nx][ny]:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

            # 조건문 구조 바꿈으로써 속도 좀 더 빨라짐 
            # if (0 <= nx < l) and (0 <= ny < l) and not graph[nx][ny]:
            #     graph[nx][ny] = graph[x][y] + 1
            #     queue.append([nx, ny])

t = int(sys.stdin.readline())

# 나이트가 움직일 수 있는 경우
dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

# start와 end를 함수 내에서 직접 int 형태로 받음으로써 속도 더 빨라짐
for _ in range(t):
    l = int(sys.stdin.readline())
    graph = [[0]*l for i in range(l)]
    # start = list(map(int, sys.stdin.readline().split()))
    # end = list(map(int, sys.stdin.readline().split()))

    print(bfs())