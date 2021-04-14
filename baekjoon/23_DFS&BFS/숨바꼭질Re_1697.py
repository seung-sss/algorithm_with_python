import sys
from collections import deque

# def bfs(start, end):
#     count = 0
#     q = deque([[start, count]])
#
#     while q:
#         tmp = q.popleft()
#         now = tmp[0]
#         count = tmp[1]
#
#         if not visited[now]:
#             visited[now] = True
#             if now == end:
#                 return count
#             count += 1
#
#             if (now * 2) <= 100000:
#                 q.append([now * 2, count])
#             if (now + 1) <= 100000:
#                 q.append([now + 1, count])
#             if (now - 1) >= 0:
#                 q.append([now - 1, count])
#
#     return count

# 다른 방법 (시간 효율성이 좀 더 높음)
def bfs(n, k, visited):
    queue = deque()
    queue.append(n)

    while queue:
        n = queue.popleft()
        if n == k:
            return visited[n]

        for nx in [n+1, n-1, n*2]:
            # 0이 아닌 곳은 이미 최소값으로 방문된 곳임으로 넘겨도 됨
            if (0 <= nx <= 100000) and (visited[nx] == 0):
                visited[nx] = visited[n] + 1
                queue.append(nx)

n, k = map(int, sys.stdin.readline().split())
# visited = [False] * 100001
visited = [0] * 100001
print(bfs(n, k, visited))
