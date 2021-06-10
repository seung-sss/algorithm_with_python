def solution(nums):
    # setnums = list(set(nums))
    # return len(nums) // 2 if len(setnums) > len(nums) // 2 else len(setnums)

    return min(len(nums) // 2, len(set(nums)))

nums1 = [3, 1, 2, 3]
print(solution(nums1))
# answer : 2

nums2 = [3, 3, 3, 2, 2, 4]
print(solution(nums2))
# answer : 3

nums3 = [3, 3, 3, 2, 2, 2]
print(solution(nums3))
# answer : 2