import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    tmp = sys.stdin.readline().split()
    # 이름은 문자열, 점수는 int로 변환하여 저장
    arr.append((tmp[0], int(tmp[1])))

# 점수 기준으로 정렬
res = sorted(arr, key=lambda x: x[1])

for val in res:
    print(val[0], end=' ')