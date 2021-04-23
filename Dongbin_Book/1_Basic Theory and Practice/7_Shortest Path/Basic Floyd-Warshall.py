# '모든 지점에서 다른 모든 지점까지의 최단 경로 모두 구해야 하는 경우' 사용하는 알고리즘
# 거쳐가는 노드를 기준으로 해당 노드 거쳐서 가는 경로와, 기존 테이블에 작성된 경로 중 최단 거리값으로 갱신
# 시간 복잡도는 O(N^3)
# 점화식 : Dab = min(Dab, Dak + Dkb)
# 즉, 'a에서 b로 가는 최소 비용' vs 'a에서 k를 거쳐 b로 가는 비용' 비교하여 더 작은 값으로 갱신
# 2차원 리스트에 최단 거리 정보 담음
# 초기에는 리스트 무한값으로 초기화 + 자기 자신에서 자기 자신으로 가는 부분은 0으로 초기화
# + 초기 간선 정보를 전부 리스트에 넣어 초기화
# 이후 점화식에 맞춰 알고리즘 수행

import sys

# 무한 의미하는 값으로 10억 설정
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수 및 간선 개수 입력받기
n = int(input())
m = int(input())

# 2차원 리스트 만들고, 모든 값 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용 0으로 초기화
for i in range(1, n + 1):
    graph[i][i] = 0

# 각 간선에 대한 정보 입력받아, 그 값으로 초기화
for _ in range(m):
    # a에서 b로 가는 비용은 c라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 수행 결과물 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print('INFINITY', end=' ')
        else:
            print(graph[i][j], end=' ')
    print()