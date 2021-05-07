from collections import defaultdict, deque


def solution(record):
    answer = []
    nickname = defaultdict(str)
    q = deque()

    for rec in record:
        tmp = rec.split()

        if tmp[0] == 'Enter':
            nickname[tmp[1]] = tmp[2]

        elif tmp[0] == 'Change':
            nickname[tmp[1]] = tmp[2]

        q.append((tmp[0], tmp[1]))

    while q:
        cmd, uid = q.popleft()

        if cmd == 'Enter':
            answer.append("%s님이 들어왔습니다." % nickname[uid])

        elif cmd == 'Leave':
            answer.append("%s님이 나갔습니다." % nickname[uid])

    return answer
# 딕셔너리로 키는 유저 아이디 / 밸류는 닉네임으로 최신값 갖기
# 각각의 record는 큐에 넣기(명령, 아이디만)
# 순서대로 빼며 유저 아이디 맞춰 출력