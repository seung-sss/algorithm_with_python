# DFS 메서드 정의출
# DFS는 스택 자료구조를 이용함 (스택 이용 시, 재귀함수 이용하면 효과적으로 코드 작성 가능)
def dfs(graph, start, visited):
    # 현재 노드 방문 처리
    visited[start] = True
    print(start, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for loc in graph[start]:
        if not visited[loc]:
            dfs(graph, loc, visited)

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

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] * 9

# dfs함수 호
dfs(graph, 1, visited)