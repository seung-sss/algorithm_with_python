# i번째 식량창고 최적의 해 구할 때 왼쪽부터 (i-3)번째 이하 식량창고에 대한 최적의 해 고려할 필요 없음
# 왜냐하면 d[i-3]은 d[i-1]과 d[i-2] 구하는 과정에서 이미 계산되었기(고려되었기) 때문임
import sys

n = int(sys.stdin.readline())
# 식량 정보 입력
food = list(map(int, sys.stdin.readline().split()))

# DP 테이블 생성
d = [0] * 100

# DP 진행
d[0] = food[0]
d[1] = max(food[0], food[1])

# 점화식 : A(i) = max(A(i-1), A(i-2) + K(i))
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + food[i])

print(d[n - 1])