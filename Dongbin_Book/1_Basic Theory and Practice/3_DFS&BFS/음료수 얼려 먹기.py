# dfs 이용 (반드시 다시 보며 익혀보기!)
import sys

n, m = map(int, sys.stdin.readline().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

# for문 돌며 해당 칸이 0인 경우, dfs로 연결된 모든 0을 탐색하고 방문처리(1로 변경)
def dfs(x, y):
    # 주어진 범위 벗어나는 경우 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    # 현재 노드 방문하지 않았다면
    if graph[x][y] == 0:
        #해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우 위치 모두 재귀적 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True # 연결된 모든 곳 방문처리 되고, 최종적으로 True값 리턴
    return False # 만일 해당 지점이 1이면, 바로 False 처리

res = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            res += 1

print(res)

