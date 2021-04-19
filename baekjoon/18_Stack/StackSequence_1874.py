import sys

n = int(sys.stdin.readline())
stk = []
res = []
cnt = 1
state = True

for _ in range(n):
    tmp = int(sys.stdin.readline())
    while cnt <= tmp:
        stk.append(cnt)
        res.append('+')
        cnt += 1

    if stk[-1] == tmp:
        stk.pop()
        res.append('-')
    else:
        state = False

if state:
    for val in res:
        print(val)
else:
    print('NO')