import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda x: (x[1], x[0])) # key에 2개 인자 주면 인자 순서대로 정렬

res = 0
now = 0

for val in arr:
    if now <= val[0]:
        res += 1
        now = val[1]

print(res)

# 첫 번째 회의는 무조건 넣고 시작하는 방법 (딱히 더 효율성은 x)
# res = 1
# eTime = arr[0][1]
# for i in range(1, n):
#     if arr[i][0] >= eTime:
#         res += 1
#         eTime = arr[i][1]
#
# print(res)