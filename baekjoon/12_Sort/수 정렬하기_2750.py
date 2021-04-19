# 데이터 1000개 정도는 기본 라이브러리 이용이 나을 듯
import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]

arr.sort()

for val in arr:
    print(val)

# 계수 정렬 이용하기
# 오히려 라이브러리보다 시간 더 걸림
# num = [False for _ in range(2001)]
#
# for val in arr:
#     num[val+1000] = True
#
# for i in range(len(num)):
#     if num[i]:
#         print(i-1000)