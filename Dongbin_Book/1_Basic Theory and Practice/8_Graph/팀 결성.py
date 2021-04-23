# 서로소 집합 알고리즘 문제
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

for i in range(n + 1):
    parent[i] = i

# 각 연산 하나씩 확인
for _ in range(m):
    ins, a, b = map(int, sys.stdin.readline().split())

    # 연산이 0이면 합치기 실행
    if ins == 0:
        union_parent(parent, a, b)
    # 연산이 1이면 두 원소가 같은 루트 노드 갖고 있는지 확인하여 유무 출력
    elif ins == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')