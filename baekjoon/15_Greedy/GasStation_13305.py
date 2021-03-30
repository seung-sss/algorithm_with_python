import sys # 시간초과 난 알고리즘

n = int(sys.stdin.readline())
dist = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))[:-1]

res = 0
while price:
    spot = min(price)
    idx = price.index(spot)
    res += sum(dist[idx:]) * spot
    dist = dist[:idx]
    price = price[:idx]

print(res)