import sys

n = int(sys.stdin.readline())
dist = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))[:-1]

min_price = 1000000001
res = 0

for i in range(len(price)):
    if price[i] < min_price:
        min_price = price[i]
    res += (min_price * dist[i])

print(res)

# for문을 돌면서 해당 지점 price가 기존 min_price보다 저렴하면 min_price 교체
# 각 지점마다 min_price 가격만큼 거리 곱해주면 됨!
# for문 한번 돌면 되기 때문에 O(n) 복잡도 가짐