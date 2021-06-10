# Summer/Winter Coding(~2018)
# 소수 판별 부분 더 효율적인 방법 찾아보기!

from itertools import combinations


# def is_prime(num):
#     if num == 1:
#         return False

#     for i in range(2, num):
#         if num % i == 0:
#             return False

#     return True

# def solution(nums):
#     answer = 0
#     for val in combinations(nums, 3):
#         if is_prime(sum(val)):
#             answer += 1

#     return answer

def is_prime(x):
    if x == 1:
        return 0

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return 0
    return 1


def solution(nums):
    return sum([is_prime(sum(c)) for c in combinations(nums, 3)])

nums1 = [1, 2, 3, 4]
print(solution(nums1))
# answer : 1

nums2 = [1, 2, 7, 6, 4]
print(solution(nums2))
# answer : 4