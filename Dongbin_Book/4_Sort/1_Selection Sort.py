# 가장 작은 데이터를 맨 앞의 데이터와 바꾸고, 그다음 작은 데이터를 앞에서 두 번째 데이터와 바꾸는 과정 반복
# (N-1)번 만큼 가장 작은 수 찾아서 앞으로 보내야 함 + 매번 가장 작은 수 찾기 위한 비교 연산 필요
# 연산 횟수는 N + (N-1) + (N-2) + ... + 2
# 근사값으로 N * (N-1) / 2 = (N^2 + N) / 2
# 따라서 시간 복잡도는 항상 O(N^2)임
# 기본 정렬 라이브러리 이용하는 것이 더 효율적

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = i
    for j in range(i+1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j

    array[i], array[min_idx] = array[min_idx], array[i]

print(array)