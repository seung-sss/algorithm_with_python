import sys
from collections import deque

def bfs(x):
    queue = deque()
    queue.append(x)
    bi[x] = 1

    while queue:
        tmp = queue.popleft()

        for val in graph[tmp]:
            if bi[val] == 0:
                bi[val] = -bi[tmp]
                queue.append(val)

            elif bi[val] == bi[tmp]:
                return False

    return True

t = int(sys.stdin.readline())
for _ in range(t):
    v, e = map(int, sys.stdin.readline().split())

    graph = [[] for i in range(v+1)]
    bi = [0 for _ in range(v+1)]

    for i in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    # 이 부분 제거하고 제출 시 틀렸음
    # 만일 그래프가 독립적으로 연결되지 않은 정점이 존재하는 경우 탐색 위해
    # 이 조건을 넣지 않으면 틀리게 되는 것
    ans = True
    for i in range(1, v+1):
        if bi[i] == 0:
            ans = bfs(i)
            if not ans:
                break

    if ans:
        print('YES')
    else:
        print('NO')
