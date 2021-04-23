import sys
from collections import deque
import copy

# n : 가로, 세로 크기 / k : 바이러스 종류
n, k = map(int, sys.stdin.readline().split())
# graph : 전체 시험관 정보
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# s : 확인 시점(초) / (x, y) : 확인할 위치
s, x, y = map(int, sys.stdin.readline().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, virus):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus

for _ in range(s):
    temp = copy.deepcopy(graph)

    for virus in range(1, k + 1):
        for i in range(n):
            for j in range(n):
                if temp[i][j] == virus:
                    bfs(i, j, virus)

print(graph[x-1][y-1])

