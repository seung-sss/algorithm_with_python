# 2019 카카오 개발자 겨울 인턴십

from collections import deque


def solution(board, moves):
    answer = 0
    stack = []
    board_list = [deque() for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board)):
            if board[j][i] != 0:
                board_list[i].append(board[j][i])

    for val in moves:
        if board_list[val - 1]:
            tmp = board_list[val - 1].popleft()
            if stack and stack[-1] == tmp:
                stack.pop()
                answer += 2
            else:
                stack.append(tmp)

    return answer

board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, moves))
# answer : 4