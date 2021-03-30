import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
stack = [] # 인덱스 값을 넣음
res = [-1 for _ in range(n)]

for i in range(n):
    while stack and num[stack[-1]] < num[i]:
        res[stack.pop()] = num[i]
    stack.append(i)

# for val in res:
#     print(val, end = ' ')

print(*res)
