# 자료구조 수업에서 배운 내용을 추가함
# 배열에서 i번째 값과 i+1번째 값을 비교하며 자리 바꿈
# 더 이상 교환이 발생 안하면 종료시킴
# 시간 복잡도는 O(N^2)이지만, 최상의 경우 O(N)의 복잡도 가짐

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

while True:
    exitYN = True
    for i in range(0, len(array)-1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            exitYN = False

    if exitYN:
        break

print(array)