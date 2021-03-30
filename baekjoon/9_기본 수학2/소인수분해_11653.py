import sys

n = int(sys.stdin.readline())
# i = 2

# while n != i:
#     if n % i == 0:
#         n = n // i
#         print(i)
#     else:
#         i += 1
#
# print(n)

# 시간초과 풀이

while n != 1:
    for i in range(2, n+1):
        if n % i == 0:
            print(i)
            n = n // i
            break