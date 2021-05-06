import sys
import copy

n = int(sys.stdin.readline())
graph = [sys.stdin.readline().split() for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = False

def look(x, y, arr):
    global res

    if x < 0 or x >= n or y < 0 or y >= n or arr[x][y] == 'O':
        return

    if arr[x][y] == 'S':
        res = True
        return

    look(x - 1, y, arr)
    look(x + 1, y, arr)
    look(x, y - 1, arr)
    look(x, y + 1, arr)

def dfs(count):
    global res

    if count == 3:
        tmp = copy.deepcopy(graph)

        for i in range(n):
            for j in range(n):
                if tmp[i][j] == 'T':
                    look(i, j, tmp)
                    if res:
                        res = False
                        return
                    else:
                        return 'YES'

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                count += 1
                dfs(count)
                graph[i][j] = 'X'
                count -= 1

    return 'NO'

print(dfs(0))