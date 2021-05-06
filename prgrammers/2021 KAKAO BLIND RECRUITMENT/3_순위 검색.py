from itertools import combinations


def solution(info, query):
    answer = []
    info_dict = dict()

    for inf in info:
        tmp = inf.split()
        inf_key = tmp[:-1]
        inf_val = int(tmp[-1])

        for i in range(5):
            for c in combinations(inf_key, i):
                tmp_key = "".join(c)

                if tmp_key in info_dict:
                    info_dict[tmp_key].append(inf_val)
                else:
                    info_dict[tmp_key] = [inf_val]

    for val in info_dict.keys():  # 각 value 정렬
        info_dict[val].sort()

    for q in query:
        tmp = q.split()
        q_key = tmp[:-1]
        q_val = int(tmp[-1])

        while 'and' in q_key:
            q_key.remove('and')
        while '-' in q_key:
            q_key.remove('-')

        tmp_key = ''.join(q_key)

        if tmp_key in info_dict:
            score = info_dict[tmp_key]

            if score:
                start, end = 0, len(score)

                while start < end:
                    mid = (start + end) // 2

                    if score[mid] >= q_val:
                        end = mid
                    else:
                        start = mid + 1

                answer.append(len(score) - start)
        else:
            answer.append(0)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
# 정답 : [1, 1, 1, 1, 2, 4]