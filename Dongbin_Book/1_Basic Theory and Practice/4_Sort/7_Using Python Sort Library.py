# 라이브러리 이용하는 것이 효과적인 경우 많음
# 기본 정렬 라이브러리 sorted() 함수는 병합 정렬 기반
# 정확히는 병합 정렬과 삽입 정렬의 아이디어 더한 하이브리드 방식 정렬 알고리즘 이용
# 최악의 경우에도 시간 복잡도 O(NlogN) 보장함
# 집합, 딕셔너리 자료형 입력받아도 반환 결과는 리스트 자료형임
# 최종적으로 단순 정렬해야 하는 상황에서는 라이브러리 사용!
# 데이터 범위 한정되고 더 빠르게 동작해야 할 때는 계수 정렬 사용!


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# sorted() 함수 이용
# 별도의 정렬된 리스트가 반환
result = sorted(array)
print(result)

# 리스트 내장 함수 sort() 이용
# 내부 원소가 바로 정렬
array.sort()
print(array)

# sorted() or sort() 이용할 때 key를 매개변수로 입력받을 수 있음
# key 값으로 하나의 함수 들어가야 하고 이는 정렬 기준이 됨
# 이를 위해 일반 함수 or 람다(lambda) 함수 이용 가능
array2 = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result2 = sorted(array2, key=setting, reverse=False)
print(result2)

result3 = sorted(array2, key=lambda x: x[1])
print(result3)


# cf> lambda식 이용
a = [(1, 2), (0, 1), (5, 1), (5, 2), (3, 0)]

# 인자없이 그냥 sorted()만 쓰면, 리스트 아이템의 각 요소 순서대로 정렬을 한다.
b = sorted(a)
# b = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

# key 인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 순서대로 정렬한다.
c = sorted(a, key = lambda x : x[0])
# c = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]
d = sorted(a, key = lambda x : x[1])
# d = [(3, 0), (0, 1), (5, 1), (1, 2), (5, 2)]

# 아이템 첫 번째 인자를 기준으로 오름차순으로 먼저 정렬하고,
# 그리고 그 안에서 다음 두 번째 인자를 기준으로 내림차순으로 정렬하게 하려면, 다음과 같이 할 수 있다.
e = [(1, 3), (0, 3), (1, 4), (1, 5), (0, 1), (2, 4)]
f = sorted(e, key = lambda x : (x[0], -x[1]))
# f = [(0, 3), (0, 1), (1, 5), (1, 4), (1, 3), (2, 4)]