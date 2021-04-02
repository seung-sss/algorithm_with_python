import sys
from collections import deque
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            # if nx < 0 or ny < 0 or nx >= n or ny >= m:
            #     continue
            #
            # if graph[nx][ny] == 1:
            #     graph[nx][ny] = graph[a][b] + 1
            #     queue.append((nx, ny))

            # 통과 조건만 걸어둘 경우, 시간 효율성이 더 높았음
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[a][b] + 1
                    queue.append((nx, ny))

    return graph[n-1][m-1]

n, m = map(int, sys.stdin.readline().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))
