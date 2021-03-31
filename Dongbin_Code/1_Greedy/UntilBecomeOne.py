import sys
import time

n, k = map(int, sys.stdin.readline().split())

# sTime = time.time()
# cnt = 0
# while n != 1:
#     if n % k == 0:
#         n = n / k
#         cnt += 1
#     else:
#         n -= 1
#         cnt += 1
#
# print(cnt)
# eTime = time.time()
# print(eTime - sTime)

sTime = time.time()
cnt = 0
while True:
    if n < k:
        cnt += n - 1
        break
    else:
        tmp = n % k
        cnt += tmp
        n = (n-tmp) // k
        cnt += 1

print(cnt)
eTime = time.time()
print(eTime - sTime)