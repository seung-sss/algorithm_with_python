from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    # 각 주문들 정렬
    orders = [sorted(i) for i in orders]
    # 디폴트 값이 int(즉, 0임)
    counter = defaultdict(int)
    max_count = defaultdict(int)

    for order in orders:
        for c in course:
            if len(order) < c:
                continue
            combination = combinations(order, c)
            for each in combination:
                food = "".join(each)

                counter[food] += 1

                if max_count[c] < counter[food]:
                    max_count[c] = counter[food]

    answer = []

    for c in course:
        if max_count[c] < 2: continue
        answer += [i[0] for i in counter.items() if len(i[0]) == c and i[1] == max_count[c]]

    return sorted(answer)

orders_1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course_1 = [2,3,4]
# 정답 : ["AC", "ACDE", "BCFG", "CDE"]

orders_2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course_2 = [2,3,5]
# 정답 : ["ACD", "AD", "ADE", "CD", "XYZ"]

orders_3 = ["XYZ", "XWY", "WXA"]
course_3 = [2,3,4]
# 정답 : ["WX", "XY"]