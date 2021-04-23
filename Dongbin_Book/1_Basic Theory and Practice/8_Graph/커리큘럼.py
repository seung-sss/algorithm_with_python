import sys
from collections import deque
import copy

# 노드 개수 입력 받기
n = int(sys.stdin.readline())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (n + 1)
# 각 노드에 연결된 간선 정보 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for _ in range(n + 1)]
# 각 강의 시간을 0으로 초기화
time = [0] * (n + 1)

# 방향 그래프의 모든 간선 정보 입력 받기
for i in range(1, n + 1):
    data = list(map(int, sys.stdin.readline().split()))
    time[i] = data[0]

    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행 결과 담을 리스트
    q = deque()

    # 처음 시작 시 진입차수가 0인 노드 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()

        # result에 저장된 값과 해당 노드에 다음 노드의 강의 시간 합친 값과 비교하여 큰 것으로 변경
        # 해당 원소와 연결된 노드들의 진입차수 1 빼기
        for next in graph[now]:
            result[next] = max(result[next], result[now] + time[next])
            indegree[next] -= 1

            # 진입차수 0이 되면 큐에 넣어줌
            if indegree[next] == 0:
                q.append(next)

    for i in range(1, n + 1):
        print(result[i])

topology_sort()

