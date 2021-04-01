# bfs 이용
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

# 이동할 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4방향 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 공간 범위 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 해당 노드 첫 방문 시 최단 거리 기록 (1인 경우, 아직 방문하지 않은 곳)
            # 이 노드 값을 다른 값으로 변경해주면 이는 최단 거리인 동시에 방문처리 되는 것
            # 이에 따라 시작 노드는 값이 3으로 변할 수 있으나 여기서는 상관 없으므로 무시
            # 이 if문에 걸리지 않는 괴물이 있는 영역은 자동으로 무시됨
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 모든 연산 끝나면 탈출구 있는 노드에 기록된 값이 최단 기록 값임
    return graph[n-1][m-1]

# bfs 수행결과 출력
print(bfs(0,0))

