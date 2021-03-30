import sys
import time

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort()

sTime = time.time()
for i in range(1, n):
    arr[i] = arr[i-1] + arr[i]

print(sum(arr))
eTime = time.time()
print(eTime - sTime)

# 아래 코드가 더 시간효율성 좋음
# sTime = time.time()
# res = 0
# for i in range(n):
#     res += arr[i] * (n-i)
#
# print(res)
# eTime = time.time()
# print(eTime - sTime)