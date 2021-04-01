import sys
from collections import deque

# 스택 이용
def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        tmp = stack.pop()
        if tmp not in visited:
            visited.append(tmp)
            stack += reversed(graph[tmp])

    return visited

# 재귀 이용
def recur_dfs(graph, start, visited):
    if start not in visited:
        visited.append(start)

        for loc in graph[start]:
            recur_dfs(graph, loc, visited)

    return visited

# 큐 이용
def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        tmp = queue.popleft()
        if tmp not in visited:
            visited.append(tmp)
            queue += graph[tmp]

    return visited

n, m, v = map(int, sys.stdin.readline().split())
graph = {i:[] for i in range(1, n+1)}
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for val in graph.keys():
    graph[val].sort()

# 스택 이용 dfs 출력
print(' '.join(list(map(str, dfs(graph, v)))))
# 재귀 이용 dfs 출력
print(' '.join(list(map(str, recur_dfs(graph, v, visited=[])))))
# 큐 이용 bfs 출력
print(' '.join(list(map(str, bfs(graph, v)))))
