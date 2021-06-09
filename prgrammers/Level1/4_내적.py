# 월간 코드 챌린지 시즌1

def solution(a, b):
    #     answer = 0

    #     for i in range(len(a)):
    #         answer += a[i] * b[i]

    #     return answer

    return sum(x * y for x, y in zip(a, b))

a1 = [1, 2, 3, 4]
b1 = [-3, -1, 0, 2]
print(solution(a1, b1))
# answer : 3

a2 = [-1, 0, 1]
b2 = [1, 0, -1]
print(solution(a2, b2))
# answer : -2