# dfs 이용
import sys

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return 0

    if graph[x][y] == 1:
        graph[x][y] = 0

        return 1 + dfs(x-1, y) + dfs(x+1, y) + dfs(x, y-1) + dfs(x, y+1)

    return 0

res = 0
size = []
for i in range(n):
    for j in range(n):
        tmp = dfs(i, j)
        if tmp != 0:
            res += 1
            size.append(tmp)

size.sort()

print(res)
for val in size:
    print(val)
