# 다익스트라 알고리즘은 그래프에서 여러 노드가 있을 때,
# 특정 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로 구해주는 알고리즘
# 그리디 알고리즘의 일종으로, 매번 '가장 비용이 적은 노드' 선택해서 임의의 과정 반복함
# 원리 설명
# 1. 출발 노드를 설정한다.
# 2. 최단 거리 테이블을 초기화한다.
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택한다.
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신한다.
# 5. 3, 4의 과정을 반복한다.
# 최단 경로 구하는 과정에서 '각 노드에 대한 현재까지의 최단 거리' 정보를
# 항상 1차원 리스트에 저장하며 리스트를 계속 갱신하는 특징이 있음(최단 거리 테이블)

# 한 단계당 하나의 노드에 대한 최단 거리르 확실히 찾는 것으로 이해할 수 있음
# 즉, 방문처리 된 노드는 이미 최단 거리를 찾은 것임(이후에는 처리되는 과정에서 값이 갱신되지 않을 것!)
# 기본 다익스트라 알고리즘은 O(V^2)의 시간복잡도 가짐 (V = 노드의 개수)
# '방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택' 위해 매 단계마다 1차원 리스트 순차 탐색함!
# 만일 최단 경로 구해야 한다면, distance 리스트에 거리값과 이전에 거쳐온 노드 함께 저장하면 됨!
# 이후 종료점에서 역으로 이전 노드를 순서대로 뽑아 reverse 시키면 최단 경로 나옴!

# 모든 리스트는 (노드 개수 + 1)로 할당하여 노드 번호를 인덱스로 이용하여 바로 리스트 접근할 수 있도록 함

import sys
input = sys.stdin.readline
INF = int(1e9) # 무한 의미하는 값으로 10억을 설정

# 노드 개수, 간선 개수 입력 받기
n, m = map(int, input().split())

# 시작 노드 번호 입력받기
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보 담는 리스트 만들기
graph = [[] for _ in range(n + 1)]

# 방문한 적 있는지 체크하는 리스트 만들기
visited = [False] * (n + 1)

# 최단 거리 테이블 만들고 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True

    # 시작 노드와 연결된 노드들의 거리값 업데이트
    for next in graph[start]:
        distance[next[0]] = next[1]

    # 시작 노드 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 잛은 노드 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True

        # 현재 노드와 연결된 다른 노드를 확인
        for next in graph[now]:
            # 현재 노드 거쳐서 다른 노드 갔을 때의 거리값 계산
            cost = distance[now] + next[1]

            # 현재 노드 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 거리값 갱신
            if cost < distance[next[0]]:
                distance[next[0]] = cost

# 다익스트라 알고리즘 실행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
    # 도달 할 수 없는 경우, 무한(INFINITY)라고 출력
    if distance[i] == INF:
        print('INFINITY')
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])

