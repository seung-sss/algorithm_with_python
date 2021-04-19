import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
que = deque([i+1 for i in range(n)])

print('<', end = '')
while len(que) > 1:
    for _ in range(k-1):
        que.append(que.popleft())
    print(str(que.popleft()) + ', ', end = '')
print(str(que.pop()) + '>')

# 인덱스 이용한 풀이
# N, K = map(int, input().split())
# stack = [i for i in range(1, N + 1)]
# result = []
# temp = K - 1
#
# for i in range(N):
#     if len(stack) > temp:
#         result.append(stack.pop(temp))
#         temp += K - 1
#     elif len(stack) <= temp:
#         temp = temp % len(stack)
#         result.append(stack.pop(temp))
#         temp += K - 1
#
# print("<", end='')
# for i in result:
#     if i == result[-1]:
#         print(i, end = '')
#     else:
#         print("%s, " %(i), end='')
# print(">")