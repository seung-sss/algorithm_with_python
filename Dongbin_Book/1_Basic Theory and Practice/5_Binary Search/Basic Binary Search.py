# 이진탐색은 찾으려는 데이터와 중간점 위치에 있는 데이터 반복적으로 비교하여 탐색하는 것
# 시간 복잡도 O(logN)임
# 데이터가 정렬되어 있어야 사용할 수 있음
# mid값과 비교하며 탐색 필요 없는 부분을 계속 제거하는 것
# 이진탐색 코드는 암기가 되어야 됨
# 시험에서 탐색 범위가 2000만을 넘어가면 이진 탐색 접근해보길 권함
# 처리해야 할 테이터의 개수나 값이 1000만 단위 이상 넘어가면 이진 탐색과 같은 O(logN) 속도 내야하는 알고리즘 떠올려야 함

import sys

# 재귀 이용
def binary_search_recur(array, target, start, end):
    # array에 target이 없는 경우 None 리턴
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target: # 값을 찾은 경우 해당 인덱스 리턴
        return mid
    # mid보다 값이 작은 경우, (mid-1)로 end값 변경
    elif array[mid] > target:
        return binary_search_recur(array, target, start, mid-1)
    # mid보다 값이 큰 경우, (mid+1)로 start값 변경
    else:
        return binary_search_recur(array, target, mid+1, end)

# 반복문 이용
def binary_search_rep(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

# n : 원소 개수 / target : 찾을 값
n, target = map(int, sys.stdin.readline().split())
# array : 전체 원소
array = list(map(int, sys.stdin.readline().split()))

# 재귀 결과
res_recur = binary_search_recur(array, target, 0, n-1)
if res_recur == None:
    print('원소가 존재하지 않습니다.')
else:
    print(res_recur+1)

# 반복문 결과
res_rep = binary_search_rep(array, target, 0, n-1)
if res_rep == None:
    print('원소가 존재하지 않습니다.')
else:
    print(res_rep+1)