# 다익스트라 알고리즘 이용
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# n : 도시 개수 / m : 통로 개수 / c : 메세지 보내고자 하는 도시
n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

# x도시에서 y도시로 가는 비용 z
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            cost = distance[now] + next[1]

            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

dijkstra(c)

# 도달할 수 있는 노드의 개수
count = 0
# 도달 가능 노드 중에서 가장 멀리 있는 노드와의 최단 거리
max_distance = 0

for val in distance:
    # 도달 가능한 경우
    if val != INF:
        count += 1
        max_distance = max(max_distance, val)

# 시작 노드 제외해야 하므로 count - 1 해줌
print(count - 1, max_distance)
