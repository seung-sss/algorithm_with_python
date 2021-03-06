# 타일링 문제
# 가로 길이를 하나씩 늘려가며 가능한 경우의 수를 구해준다!
# 가로 길이가 1인 경우의 수는 1가지 / 가로 길이가 2인 경우의 수는 3가지임
# 가로 길이가 3인 경우
# 1. 가로 길이가 2인 경우에 (2*1) 타일 붙여주는 것
# 2. 가로 길이가 1인 경우에 (1*2) 타일 두 장 붙여주는 것 + (2*2) 타일 붙여주는 것
# 따라서, (d[i-1]의 경우의 수 * 1가지 경우의 수) + (d[i-2]의 경우의 수 * 2가지 경우의 수)
# 점화식 : A(i) = A(i-1) + (A(i-2) * 2)
# 타일의 가로 길이가 최대 2이기 때문에 i-2까지만 고려하면 됨
# (i-1)과 (i-2) 이전의 경우의 수는 이미 계산된 것으로 고려할 필요가 없음

import sys

n = int(sys.stdin.readline())

d = [0] * 1001
d[1] = 1
d[2] = 3

for i in range(3, n + 1):
    d[i] = d[i - 1] + (d[i - 2] * 2)

print(d[n])

# cf> (1*2), (2*1) 타일만 존재하는 경우
# d[i-1]에 (2*1) 타일 붙이는 경우 1가지 + d[i-2]에 (1*2) 타일 두 장 붙이는 경우 1가지

d2 = [0] * 1001
d2[1] = 1
d2[2] = 2

for i in range(3, n + 1):
    d2[i] = d2[i - 1] + d2[i - 2]

print(d2[n])
