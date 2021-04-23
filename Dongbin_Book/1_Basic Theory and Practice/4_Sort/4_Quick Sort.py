# pivot이라는 기준 데이터를 설정하고 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 것
# 위치 교환 후, 리스트를 나눠 각 부분에서 다시 정렬하는 것
# 아래 코드는 '리스트에서 첫 번재 데이터를 pivot으로 이용'하는 호어 분할 방식임
# 왼쪽부터 pivot보다 큰 데이터 찾고, 오른쪽부터 pivot보다 작은 데이터 찾음
# 이후 둘의 위치를 교환해줌
# 왼쪽 부분과 오른쪽 부분이 엇갈린 경우, 작은 데이터와 pivot 위치를 변경하여 분할시킴
# 이후 다시 왼쪽 부분과 오른쪽 부분에서 정렬을 해줌 (이를 위해 재귀 이용 방법 좋음)
# 재귀 함수에서 종료 조건은 해당 재귀에서 다루는 리스트의 데이터 개수가 1인 경우!
# 시간 복잡도는 평균 O(NlogN)이지만 최악의 경우 O(N^2)의 시간 복잡도 가짐
# 무작위로 데이터가 입력된 경우 빠르게 동작하지만,
# 리스트 가장 왼쪽 데이터 pivot으로 이용하는 경우, '이미 데이터가 정렬되어 있는 경우' 매우 느리게 동작

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소 1개인 경우 종료
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 왼쪽부터 pivot보다 큰 값을 찾는 것으로, 큰 값 찾을 때가지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 오른쪽부터 pivot보다 작은 값을 찾는 것으로, 작은 값 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right: # 엇갈렸다면, 작은 데이터와 pivot을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면, 작은 데이터와 큰 데이터 교체
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

# 파이썬의 장점을 살려 작성한 코드
# 전통적 방식보다 pivot과 데이터 비교 연산 횟수 증가하여 시간 면에서는 조금 비효율적이나
# 직관적이라는 점에서 장점이 있음
def simple_quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return simple_quick_sort(left_side) + [pivot] + simple_quick_sort(right_side)

print(simple_quick_sort(array))