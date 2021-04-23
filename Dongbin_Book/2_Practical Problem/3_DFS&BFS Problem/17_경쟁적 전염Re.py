import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
graph = [] # 전체 시험관 정보
data = [] # 바이러스에 대한 정보

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(n):
        # 해당 위치에 바이러스 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 x, 위치 y) 삽입
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, sys.stdin.readline().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    virus, s, x, y = q.popleft()

    if s == target_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])