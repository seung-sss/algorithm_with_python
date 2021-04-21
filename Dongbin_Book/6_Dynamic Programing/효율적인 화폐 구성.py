# 적은 금액부터 큰 금액까지 확인해가며 만들 수 있는 최소 화폐 수 DP테이블에 저장
# 점화식
# 1. A(i-k) 만드는 방법 존재하는 경우 - A(i) = min(A(i), A(i-k) + 1)
# 2. A(i-k) 만드는 방법 존재하지 않는 경우 - A(i) = 10001
# 모든 화폐를 돌아가며 각 금액을 만들 수 있는 최소값을 DP테이블에 저장

import sys

n, m = map(int, sys.stdin.readline().split())
coin = []

for _ in range(n):
    coin.append(int(sys.stdin.readline()))

d = [10001] * 10001

d[0] = 0
for i in range(n):
    for j in range(coin[i], m + 1):
        # if문 없어도 되지만 방법 존재하는 경우 설명 위해 작성 
        if d[j - coin[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - coin[i]] + 1)

if d[m] == 10001: # 최종적으로 m원 만드는 방법 없는 경우
    print(-1)
else:
    print(d[m])