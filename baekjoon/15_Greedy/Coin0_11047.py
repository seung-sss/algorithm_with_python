import sys

n, k = map(int, sys.stdin.readline().split())
coin = []

for _ in range(n):
    coin.append(int(sys.stdin.readline()))

res = 0

for i in range(n-1, -1, -1):
    if coin[i] <= k:
        res += (k // coin[i])
        k %= coin[i]
        if k == 0:
            break

print(res)