# visited 안쓰고 graph 자체의 방문한 곳의 값을 바꿨을 때 틀렸음
# 벽을 뚫지 않고도 올 수 있는 곳임에도 불구하고 그 곳을 부수고 온 애가 먼저 도착할 경우,
# 뚫어야만 갈 수 있는 곳이 오는 경우 뚫지 못하게 되어 끝까지 탐색을 못함
# 즉, 벽 부숴서 들어온애가 먼저 접근하면 안부수고 같은 자리 올 수 있는데
# 이를 못하게 되기 때문에 맵을 두 개 사용하는 방식을 이용해야 함
# 0000
# 010(0)
# 0000
# 1111
# 0000
# 괄호 부분까지 벽 안뚫고 올 수 있지만 1을 부수고 온 애가 먼저 도착하면,
# 밑에 1111로 막힌 줄을 뚫지 못하게 됨
import sys
from collections import deque

def bfs(n, m):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[[0]*m for _ in range(n)] for _ in range(2)]

    queue = deque()
    visited[0][0][0] = 1
    queue.append([0, 0, 0])

    while queue:
        x, y, z = queue.popleft()

        # 도착한 경우
        if x == n-1 and y == m-1:
            return visited[z][x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 안에 들어오고 이동할 곳이 아직 방문하지 않은 곳인 경우!
            if (0 <= nx < n) and (0 <= ny < m) and (visited[z][nx][ny] == 0):

                # 벽 안만남(그냥 길 만난 경우)
                if graph[nx][ny] == 0:
                    visited[z][nx][ny] = visited[z][x][y] + 1
                    queue.append([nx, ny, z])

                # 벽을 만났는데 아직 안 뚫어본 경우
                elif graph[nx][ny] == 1 and z == 0:
                    visited[1][nx][ny] = visited[0][x][y] + 1
                    queue.append([nx, ny, 1])

    return -1

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

print(bfs(n, m))