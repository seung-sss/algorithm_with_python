# 서로소 집합을 활용하여 사이클 판별할 수 있음
# 방법
# 1. 각 간선을 확인하며 두 노드의 루트 노드를 확인한다
# 1-1. 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산 수행한다
# 1-2. 루트 노드가 서로 같다면 사이클(Cycle)이 발생한 것이다
# 2. 그래프에 포함되어 있는 모든 간선에 대해 1번 과정 반복한다.
# 기본적인 서로소 집합 알고리즘에서 루트 노드가 같다면 사이클 발생으로 처리
# 루트 노드가 같지 않다면 원래대로 union 연산을 수행함

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

for i in range(1, v + 1):
    parent[i] = i

cycle = False # 사이클 발생 여부

for i in range(e):
    a, b = map(int, sys.stdin.readline().split())
    # 루트 노드가 같은 것은 사이클이 발생한 것으로 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클 발생하지 않았으면 합집합(union) 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print('사이클이 발생했습니다.')
else:
    print('사이클이 발생하지 않았습니다.')