import sys

n = int(sys.stdin.readline())
plan = sys.stdin.readline().rstrip().split()

x, y = 1, 1

# 내 풀이
# for val in plan:
#     if val == 'L' and y >= 2:
#         y -= 1
#     elif val == 'R' and y < n:
#         y += 1
#     elif val == 'U' and x >= 2:
#         x =- 1
#     elif val == 'D' and x < n:
#         x += 1
#
# print(x, y)

# 책 풀이
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for val in plan:
    for i in range(len(move_type)):
        if val == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue # 뒷 코드 무시하고 다시 for문 처음으로 돌아가는 것
    x, y = nx, ny

print(x, y)