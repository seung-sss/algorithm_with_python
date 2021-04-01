import sys
from collections import deque

node = int(sys.stdin.readline())
link = int(sys.stdin.readline())

graph = {i:[] for i in range(1, node+1)}
for _ in range(link):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

# bfs 이용
def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        tmp = queue.popleft()
        if tmp not in visited:
            visited.append(tmp)
            queue += graph[tmp]

    return len(visited)

print(bfs(graph, 1) - 1)
