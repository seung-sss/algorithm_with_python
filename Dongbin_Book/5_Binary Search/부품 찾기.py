import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

# n = int(sys.stdin.readline())
# n_list = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# m_list = list(map(int, sys.stdin.readline().split()))

# 기본 정렬 + 이진 탐색
# n_list.sort()
# for target in m_list:
#     res = binary_search(n_list, target, 0, n-1)
#
#     if res == None:
#         print('no', end = ' ')
#     else:
#         print('yes', end = ' ')

# 계수 정렬 + 이진 탐색
# num_arr = [0] * 1000001
# for val in n_list:
#     num_arr[val] += 1
#
# sort_list = []
# for i in range(len(num_arr)):
#     if num_arr[i] != 0:
#         sort_list.append(i)
#
# for target in m_list:
#     res = binary_search(sort_list, target, 0, n-1)
#
#     if res == None:
#         print('no', end=' ')
#     else:
#         print('yes', end=' ')

# 집합 이용 (단순히 특정 수가 등장했는지 확인만 하면 되기 때문에 이용 가능)
n = int(sys.stdin.readline())
n_set = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

## 집합 내 있는지 유무 확인이 더 효율적인 듯
for target in m_list:
    if target in n_set:
        print('yes', end=' ')
    else:
        print('no', end=' ')

## 차집합을 이용한 내 풀이
# for target in m_list:
#     target_set = set([target])
#
#     if target_set - n_set:
#         print('no', end=' ')
#     else:
#         print('yes', end=' ')