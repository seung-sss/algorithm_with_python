# 기본 방식은 find 함수가 비효율적으로 동작한다는 단점 있음
# 최악의 경우 find에서 시간복잡도 O(V)를 가져 전체 복잡도 O(VM)이 됨 (M : union 연산 개수)
# find 함수 최적화 위해 '경로 압축(Path Compression)' 적용할 수 있음
# 경로 압축은 find 함수 재귀적으로 호출한 후 부모 테이블값을 갱신하는 기법
# 이를 이용하면 find 함수 호출 이후 해단 노드의 루트 노드가 바로 부모 노드가 됨

import sys

# 특정 원소가 속한 집합 찾기 (경로 압축 이용)
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드 찾을 때까지 재귀적 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
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

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
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
print('부모 테이블 출력:', end=' ')
for i in range(1, v + 1):
    print(parent[i], end=' ')