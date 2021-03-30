import sys

ex = list(sys.stdin.readline().rstrip().split('-'))

for i in range(len(ex)):
    try:
        ex[i] = int(ex[i])
    except:
        tmp = list(map(int, ex[i].split('+')))
        ex[i] = sum(tmp)

if len(ex) == 1:
    res = ex[0]
else:
    res = (ex[0]*2) - sum(ex)

print(res)