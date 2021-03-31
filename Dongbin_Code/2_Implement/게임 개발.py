import sys

n, m = map(int, sys.stdin.readline().split())
x, y, view = map(int, sys.stdin.readline().split()) # x = row / y = col / view = 바라보는 곳
rule = {0 : (0, -1), 1 : (-1, 0), 2 : (0, 1), 3 : (1, 0)}
map = []

for _ in range(n):
    map.append(sys.stdin.readline().rstrip().split())

check = []
visit = [str(x)+str(y)]

while True:
    nx = x + rule[view][0]
    ny = y + rule[view][1]
    view = (view - 1) % 4

    if 0 <= nx < n and 0 <= ny < m: # 움직일 곳이 범위를 벗어나지 않는 경우!
        if map[nx][ny] == '0' and str(nx)+str(ny) not in visit: # 움직일 곳이 육지이고 방문하지 않은 경우!
            x = nx
            y = ny
            visit.append(str(x)+str(y))
            check = []
            continue

    check.append(view)

    if len(check) == 4:
        nx = x + rule[(view - 1) % 4][0]
        ny = y + rule[(view - 1) % 4][1]

        if 0 <= nx < n and 0 <= ny < m: # 뒤로 이동할 곳이 범위를 벗어나지 않는 경우!
            if map[nx][ny] == '0': # 뒤로 이동할 곳이 육지인 경우!
                x = nx
                y = ny
                check = []
                continue
            else:
                break
        else:
            break

print(len(visit))




