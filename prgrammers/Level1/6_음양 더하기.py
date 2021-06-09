# 월간 코드 챌린지 시즌2

def solution(absolutes, signs):
    #     answer = 0
    #     for i in range(len(absolutes)):
    #         if signs[i]:
    #             answer += absolutes[i]
    #         else:
    #             answer -= absolutes[i]

    #     return answer

    return sum(absolute if sign else -absolute for absolute, sign in zip(absolutes, signs))

absolutes1 = [4, 7, 12]
signs1 = [True, False, True]
print(solution(absolutes1, signs1))
# answer : 9

absolutes2 = [1, 2, 3]
signs2 = [False, False, True]
print(solution(absolutes2, signs2))
# answer : 0