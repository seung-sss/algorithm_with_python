import sys
import time

n, m = map(int, sys.stdin.readline().split())

# sTime = time.time()
# arr = []
#
# for _ in range(n):
#     arr.append(list(map(int, sys.stdin.readline().split())))
#
# maxi = 0
#
# for val in arr:
#     if min(val) > maxi:
#         maxi = min(val)
# eTime = time.time()
# print(eTime - sTime)

sTime = time.time()
maxi = 0

for _ in range(n):
    tmp = min(map(int, sys.stdin.readline().split()))
    if tmp > maxi:
        maxi = tmp
eTime = time.time()
print(eTime - sTime)
# print(maxi)

