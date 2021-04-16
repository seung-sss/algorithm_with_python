# 자료구조 수업에서 배운 내용을 추가함
# 분할 후, 작은 조각을 병합하는 과정에서 부분 sort를 반복하여 정렬 완성
# 반으로 나누고, 좌우측 원소가 하나가 될 때까지 재귀호출함
# 병합 과정에서 좌우측 부분을 정렬하며 합침
# 시간 복잡도는 O(NlogN)임
# divide 단계에서 분할되는 깊이는 logN으로 O(logN) 복잡도 가
# 각 깊이별 merge 단계에서 N개의 모든 데이터가 합병되며 O(N) 복잡도 가짐짐
# 최종적으로 모든 깊이(logN의 깊이)에서 병합 수행(N개 데이터)함으로 시간 복잡도 O(NlogN)임

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 두 개의 정렬된 리스트 a, b가 있을 때 이를 병합하는 알고리즘
def merge(a, b):
    res = []
    # 두 개 중 하나 이상 리스트의 원소 수가 0이 될 때까지 반복
    while len(a) > 0 and len(b) > 0:
        # 두 리스트에서 작은 값을 가진 원소를 빼서 res에 넣음
        if a[0] < b[0]:
            res.append(a.pop(0))
        else:
            res.append(b.pop(0))
    # 리스트에 원소 없으면 다른 리스트를 res에 전부 넣음
    if len(a) == 0:
        res.extend(b)
    else:
        res.extend(a)

    return res

# 재귀로 구현한 방식
def mergeSort(x):
    if len(x) <= 1:
        return x

    # 분할 과정
    mid = len(x) // 2
    left = x[:mid]
    right = x[mid:]
    # 재귀 호출
    left = mergeSort(left)
    right = mergeSort(right)
    # 분할 결과가 한 개가 되면 그 값을 리턴해서 이를 merge
    return merge(left, right)

print(mergeSort(array))