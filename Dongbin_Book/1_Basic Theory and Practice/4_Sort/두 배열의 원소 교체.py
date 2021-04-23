import sys

n, k = map(int, sys.stdin.readline().split())
arr1 = list(map(int, sys.stdin.readline().split()))
arr2 = list(map(int, sys.stdin.readline().split()))

arr1.sort() # 첫 번째 배열은 오름차순 정렬
arr2.sort(reverse=True) # 두 번째 배열은 내림차순 정렬

# 첫 번째 인덱스부터 확인하며 최대 k번 비교
for i in range(k):
    if arr1[i] < arr2[i]: # arr1 원소가 arr2 원소보다 작은 경우
        arr1[i], arr2[i] = arr2[i], arr1[i] # 두 원소 교체
    else: # arr1 원소가 arr2 원소보다 크거나 같을 때는 교체하지 않고 종료
        break

print(sum(arr1))