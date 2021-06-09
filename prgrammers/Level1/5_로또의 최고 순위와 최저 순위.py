# 2021 Dev-Matching: 웹 백엔드 개발자

def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt = lottos.count(0)
    same = len(set(lottos) & set(win_nums))

    return rank[same + cnt], rank[same]

lottos1 = [44, 1, 0, 0, 31, 25]
win_nums1 = [31, 10, 45, 1, 6, 19]
print(solution(lottos1, win_nums1))
# answer : [3, 5]

lottos2 = [0, 0, 0, 0, 0, 0]
win_nums2 = [38, 19, 20, 40, 15, 25]
print(solution(lottos2, win_nums2))
# answer : [1, 6]

lottos3 = [45, 4, 35, 20, 3, 9]
win_nums3 = [20, 9, 3, 45, 4, 35]
print(solution(lottos3, win_nums3))
# answer : [1, 1]