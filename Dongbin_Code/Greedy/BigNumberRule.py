import sys

n, m, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort(reverse=True)

# sum = 0
# cnt = 0
#
# for _ in range(m):
#     if cnt < k:
#         sum += arr[0]
#         cnt += 1
#     else:
#         sum += arr[1]
#         cnt = 0
#
# print(sum)

sum = int((m/(k+1)) * (arr[0] * k + arr[1]) + (m%(k+1)) * arr[0])
print(sum)