# 틀린 코드
import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append(1)
    visited = [False] * (v+1)
    res1, res2 = set(), set()
    res1.add(1)
    flag = 0

    while queue:
        tmp = queue.popleft()
        if visited[tmp]:
            continue
        else:
            visited[tmp] = True

        for i in range(len(graph[tmp])):
            queue.append(graph[tmp][i])
            if flag:
                res1.add(graph[tmp][i])
            else:
                res2.add(graph[tmp][i])

        if flag:
            flag = 0
        else:
            flag = 1

    if res1 & res2:
        return 'NO'
    else:
        return 'YES'

t = int(sys.stdin.readline())

for _ in range(t):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for i in range(v+1)]

    for i in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    print(bfs())