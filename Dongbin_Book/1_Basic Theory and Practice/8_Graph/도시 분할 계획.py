# 전체 그래프에서 2개의 최소 신장 트리 만들어야 함
# 이를 위해 크루스칼 알고리즘으로 최소 신장 트리 찾은 뒤,
# 이를 구성하는 간선 중 가장 비용이 큰 간선 제거하는 것

import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, sys.stdin.readline().split())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

edges = []
result = 0

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, a, b))

edges.sort()

# 전체 최소 신장 트리 만들었음
for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        max_cost = cost

print(result - max_cost)


