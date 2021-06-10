# Counter를 이용하는 방법 익히기
# 해시

from collections import defaultdict, Counter


def solution(participant, completion):
    # 내풀이

    #     people = defaultdict(int)

    #     for p in participant:
    #         people[p] += 1

    #     for c in completion:
    #         people[c] -= 1

    #     for key, value in people.items():
    #         if value == 1:
    #             return key

    # 좋은 풀이
    return list((Counter(participant) - Counter(completion)).keys())[0]

participant1 = ["leo", "kiki", "eden"]
completion1 = ["eden", "kiki"]
print(solution(participant1, completion1))
# answer : "leo"

participant2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion2 = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant2, completion2))
# answer : "vinko"

participant3 = ["mislav", "stanko", "mislav", "ana"]
completion3 = ["stanko", "ana", "mislav"]
print(solution(participant3, completion3))
# answer : "mislav"