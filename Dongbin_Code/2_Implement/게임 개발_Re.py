import sys

n, m = map(int, sys.stdin.readline().split())
# 방문 위치 저장 위한 맵 생성하여 0으로 초기화
visit = [[0] * m for _ in range(n)]
x, y, direction = map(int, sys.stdin.readline().split())
visit[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보 받기
array = []
for _ in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction = (direction - 1) % 4

# 시뮬레이션 시작
count = 1 # 방문한 곳 카운트 세기
turn_time = 0 # 회전 수 세기

while True:
    # 왼쪽 회전 및 해당 방향 위치값 만들기
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 맵의 범위 벗어나는 경우, 예외 처리
    if 0 <= nx <= n and 0 <= ny <= m:
        # 방문하지 않은 곳이면서 육지인 경우!
        if visit[nx][ny] == 0 and array[nx][ny] == 0:
            visit[nx][ny] = 1 # 방문 처리
            # 위치 이동
            x = nx
            y = ny
            count += 1 # 방문한 곳 추가하기
            turn_time = 0 # 회전 수 리셋
            continue

    # 움직이는 조건 맞추지 못하면 다시 회전 위해 회전 수 올려줌
    turn_time += 1

    # 네 방향 전부 갈 수 없는 경우!
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 움직일 곳이 범위 벗어나는 경우 예외처리 위한 조건문
        if 0 <= nx <= n and 0 <= ny <= m:
            if array[nx][ny] == 0: # 뒤로 움직일 곳이 육지인 경우 이동
                x = nx
                y = ny
                turn_time = 0
            else: # 뒤로 움직일 곳이 바다인 경우 멈춤
                break
        else: # 뒤로 움직일 곳이 범위 벗어나는 경우 멈춤
            break

print(count)





