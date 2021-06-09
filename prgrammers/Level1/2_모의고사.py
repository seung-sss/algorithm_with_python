# 완전탐

def solution(answers):
    answer = []

    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    corr = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == p1[i % 5]:
            corr[0] += 1
        if answers[i] == p2[i % 8]:
            corr[1] += 1
        if answers[i] == p3[i % 10]:
            corr[2] += 1

    max_val = max(corr)
    for i in range(3):
        if corr[i] == max_val:
            answer.append(i + 1)

    return answer

answers1 = [1, 2, 3, 4, 5]
print(solution(answers1))
# answer : [1]

answers2 = [1, 3, 2, 4, 2]
print(solution(answers2))
# answer : [1, 2, 3]