def rotate(arr):  # 90도 회전
    tmp = [[0] * len(arr) for _ in range(len(arr))]

    for i in range(len(arr)):
        for j in range(len(arr)):
            tmp[j][len(arr) - 1 - i] = arr[i][j]

    return tmp

def check(keyArr, lockArr, x, y):
    keySize = len(keyArr)
    lockSize = len(lockArr)

    boardSize = lockSize * 3
    board = [[0] * boardSize for _ in range(boardSize)]

    start = lockSize
    end = start + lockSize - 1

    for i in range(lockSize):
        for j in range(lockSize):
            board[start + i][start + j] += lockArr[i][j]

    for i in range(keySize):
        for j in range(keySize):
            board[x + i][y + j] += keyArr[i][j]

    for i in range(start, end + 1):
        for j in range(start, end + 1):
            if board[i][j] != 1:
                return False

    return True

def solution(key, lock):
    for _ in range(4):

        for x in range(len(lock) * 2):
            for y in range(len(lock) * 2):
                if check(key, lock, x, y):
                    return True

        key = rotate(key)

    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))