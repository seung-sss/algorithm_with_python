# 정렬

import heapq


def solution(array, commands):
    #     answer = []

    #     for command in commands:
    #         tmp = []
    #         for i in range(command[0] - 1, command[1]):
    #             heapq.heappush(tmp, array[i])

    #         for _ in range(command[2]):
    #             res = heapq.heappop(tmp)

    #         answer.append(res)

    #     return answer

    return list(map(lambda x: sorted(array[x[0] - 1:x[1]])[x[2] - 1], commands))

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
# answer : [5, 6, 3]