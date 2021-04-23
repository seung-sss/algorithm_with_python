# '모든 도로의 거리는 1'이라는 조건 때문에 bfs로 해결 가능한 것!

import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
distance = [None] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

def bfs(start):
    q = deque()
    q.append(start)
    distance[start] = 0

    while q:
        now = q.popleft()

        for next in graph[now]:
            if distance[next] == None:
                distance[next] = distance[now] + 1
                q.append(next)

bfs(x)

check = False
for i in range(len(distance)):
    if distance[i] == k:
        print(i)
        check = True

if not check:
    print(-1)