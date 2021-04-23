import sys

n = list(map(int, sys.stdin.readline().rstrip()))
pivot = int(len(n) / 2)

if sum(n[:pivot]) == sum(n[pivot:]):
    print('LUCKY')
else:
    print('READY')