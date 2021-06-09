# Greedy

def solution(n, lost, reserve):
    answer = 0

    total = [1] * (n + 1)
    total[0] = -1

    for val in lost:
        total[val] = 0

    for val in reserve:
        total[val] += 1

    for i in range(1, len(total) - 1):
        if total[i] == 0:
            if total[i - 1] == 2:
                total[i] = 1
                answer += 1
                total[i - 1] -= 1
            elif total[i + 1] == 2:
                total[i] = 1
                answer += 1
                total[i + 1] -= 1
        else:
            answer += 1

    if total[n] == 0:
        if total[n - 1] == 2:
            answer += 1
    else:
        answer += 1

    return answer

n1 = 5
lost1 = [2, 4]
reserve1 = [1, 3, 5]
print(solution(n1, lost1, reserve1))
# answer : 5

n2 = 5
lost2 = [2, 4]
reserve2 = [3]
print(solution(n2, lost2, reserve2))
# answer : 4
