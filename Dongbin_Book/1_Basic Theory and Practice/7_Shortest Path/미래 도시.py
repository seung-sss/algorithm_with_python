# 플로이드 워셜 알고리즘 이용
# N의 범위가 100 이하로 한정적이어서 플로이드 워셜 알고리즘 이용 가능
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(1, m + 1):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# k(소개팅)를 거쳐 x(판매)로 가야 함
x, k = map(int, input().split())

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

res = graph[1][k] + graph[k][x]

if res >= INF:
    print(-1)
else:
    print(res)