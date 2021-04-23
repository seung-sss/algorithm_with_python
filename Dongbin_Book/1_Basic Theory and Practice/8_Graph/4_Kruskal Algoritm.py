# 신장 트리 : 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
# 모든 노드를 포함하며 사이클이 존재하지 않는다는 것은 트리의 성립조건이기도 함

# 다양한 문제 상황에서 가능한 최소한의 비용으로 신장 트리 찾아야 할 경우
# ex> 모든 도시 연결할 때, 최소한의 비용으로 연결하기
# 신장 트리 중 최소 비용으로 만들 수 있는 신장트리 찾는 알고리즘이 '최소 신장 트리 알고리즘'임
# 대표적인 최소 신장 트리 알고리즘이 '크루스칼 알고리즘(Kruskal Algoritm)'임
# 가장 적은 비용으로 모든 노드 연결할 수 있음(그리디 알고리즘으로 분류됨)

# 모든 간선에 대해 정렬 수행한 뒤 가장 거리 짧은 간선부터 집합에 포함시킴
# 이 때, 사이클 발생시킬 수 있는 간선은 집합에 포함시키지 않음
# 방법
# 1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다
# 2. 간선을 하나씩 확인하며 현재의 간선이 사이클 발생시키는지 확인한다
# 2-1. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다
# 2-2. 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다
# 3. 모든 간선에 대해 2번의 과정 반복한다

# 트리와 마찬가지로 최종적으로 신장 트리에 포함되는 간선의 개수는 '노드의 개수 - 1'과 같다는 특징 있음

# 시간복잡도 O(ElogE)임 (정렬이 가장 오래걸리는 작업 / E : 간선의 개수)

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

v, e = map(int, sys.stdin.readline().split())
parent = [0] * (v + 1)

# 모든 간선을 담을 리스트와 최종 비용 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보 입력받기
for _ in range(e):
    a, b, cost = map(int, sys.stdin.readline().split())
    # 비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선 하나씩 확인하며
for edge in edges:
    cost, a, b = edge

    # 사이클 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)