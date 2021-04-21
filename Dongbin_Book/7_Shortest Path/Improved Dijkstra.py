# 우선순위 큐를 이용하여 기존의 최단 거리 노드를 선형적으로 찾는 것보다 시간 복잡도 줄일 수 있음!
# O(ElogV)의 시간복잡도를 가짐 (E : 간선의 개수 / V : 노드의 개수)
# 한 번 처리된 노드는 이미 최소값을 가진 노드로 더 이상 처리되지 않음
# 따라서 큐에서 노드 꺼내 검사하는 반복문(while문)은 노드 개수 V 이상의 횟수로 반복되지 않음
# 또한 V번 반복될 때마다 각각 자신과 연결된 간선 모두 확인함
# 따라서 '현재 우선순위 큐에서 꺼낸 노드와 연결된 다른 노드 확인'하는 총횟수는 최대 간선 개수(E)만큼 연산 수행

# 힙 자료구조를 사용하여 로그 시간으로 최단 거리 노드를 탐색할 수 있음
# 힙 자료구조를 이용하여 우선순위 큐를 구현함
# 우선순위 큐 : 우선순위가 가장 높은 데이털르 가장 먼저 삭제하는 것!
# 파이썬에서는 PriorityQueue 또는 heapq 사용 가능 (보통 heapq가 속도가 더 빨라 이를 사용하는 것 권장)
# 우선순위 큐에 데이터 묶음 [ex> (가치, 물건)] 넣으면 첫 번째 원소 기준으로 우선순위 정함 ('가치'값 기준)
# 기본으로 최소 힙 구조가 이용됨
# (최대 힙 필요하면 우선순위 기준 값에 음수(-) 붙여 넣고, 큐에서 꺼낸 후 다시 음수(-) 붙여 원래 값 돌리는 방식 이용)
# 이러한 최소 힙 개념을 다익스트라에 적용시켜 개선된 알고리즘 만들 수 있음
# 기존의 get_smallest_node()를 우선순위 큐로 대체하는 것
# 즉, '최단 거리가 가장 짧은 노드' 선택 과정을 다익스트라 최단 경로 함수 안에서 우선순위 큐 이용하는 방식으로 대체
# 우선순위 큐에서 꺼낸 노드는 최소값 갖는 노드이고,
# 해당 노드를 이미 처리한 적 있다면 무시하고, 처리한 적 없다면 처리해주면 됨

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수 입력받기
n, m = map(int, input().split())

# 시작 노드 번호 입력받기
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보 담는 리스트 만들기
graph = [[] for _ in range(n + 1)]

# 최단 거리 테이블 생성하고, 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

def dijkstra(start):
    q = []

    # 시작 노드로 가기 위한 최단 경로 0으로 설정하고, 큐에 삽입
    heapq.heappush(q, (0, start)) # (거리값, 노드 번호)
    distance[start] = 0

    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적 있는 노드라면 무시 (이미 처리된 노드는 이미 최소 거리값 가지기 때문)
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for next in graph[now]:
            cost = dist + next[1]

            # 현재 노드 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[next[0]]:
                distance[next[0]] = cost # 거리값 갱신
                heapq.heappush(q, (cost, next[0])) # 우선순위 큐에 삽입

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])