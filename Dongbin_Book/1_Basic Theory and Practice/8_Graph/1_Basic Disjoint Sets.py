# 서로소 집합이란 공통 원소가 없는 두 집합을 의미 ({1, 2} / {3, 4})
# 서로소 집합 자료구조란 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
# 서로조 집합 자료구조는 union과 find 2개의 연산으로 조작할 수 있음
# union : 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산 (그래프에서 간선으로 표현 가능)
# find : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
# 서로소 집합 계산 알고리즘은 트리 자료구조를 이용해 집합을 표현함
# 방법
# 1. union 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인
# 1-1. A와 B의 루트 노드 A', B'를 각각 찾는다
# 1-2. A'를 B'의 부모 노드로 설정한다(B'가 A'를 가리키도록 한다)
# 2. 모든 union 연산을 처리할 때까지 1번 과정 반복한다
# 구현 시, A'와 B' 중 더 번호가 작은 원소가 부모 노드 되도록 구현하는 경우 많음
# union 연산 하나씩 확인하며 서로 다른 두 원소에 대해 합집합 수행할 때,
# 각각 루트 노드 찾아서 더 큰 루트 노드가 더 작은 루트 노드 가리키도록 하면 됨
# 초기 노드의 개수(V) 크기의 부모 테이블 초기화 (모든 원소가 자기 자신 부모로 가지도록 설정)
# 실제 루트 확인할 때에는 재귀적으로 부모 거슬러 올라가서 최종 루트 노드 찾아야 함

import sys

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, sys.stdin.readline().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블에서 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산 각각 수행
for i in range(e):
    a, b = map(int, sys.stdin.readline().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합:', end=' ')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블:', end=' ')
for i in range(1, v + 1):
    print(parent[i], end=' ')