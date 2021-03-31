import sys

loc = sys.stdin.readline().rstrip()
row = int(loc[1])
col = ord(loc[0]) - ord('a') + 1
steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

res = 0
for val in steps:
    nrow = row + val[0]
    ncol = col + val[1]

    if nrow >= 1 and ncol >= 1 and nrow <= 8 and ncol <= 8:
        res += 1

print(res)

