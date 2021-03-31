from collections import deque

#BFS 메서드 정의
# BFS는 큐 자료구조를 이용함 (일반적으로 DFS에 비해 시간효율성이 높음)
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])

    # 현재 노드 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 방문하지 않은 인접노드 큐에 넣고 방문처리 반복
    while queue:
        tmp = queue.popleft()
        print(tmp, end=' ')

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들 큐에 삽입
        for loc in graph[tmp]:
            if not visited[loc]:
                queue.append(loc)
                visited[loc] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)