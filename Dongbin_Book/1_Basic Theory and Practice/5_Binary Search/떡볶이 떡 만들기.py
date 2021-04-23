import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
start, end = 0, max(arr)

res = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for val in arr:
        # 잘랐을 때 떡의 양을 계산
        if val > mid:
            total += (val - mid)

    # 떡 양이 부족한 경우, 더 크게 잘라야 함(절단기 높이 낮춰야 함으로 왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡 양이 충분한 경우, 더 작게 잘라야 함(절단기 높이 높여야 함으로 오른쪽 부분 탐색)
    else:
        res = mid # 최대한 덜 잘랐을 때가 정답으로, 여기에서 res 기록
        start = mid + 1

print(res)