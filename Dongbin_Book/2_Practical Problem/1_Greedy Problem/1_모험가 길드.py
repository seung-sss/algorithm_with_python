import sys

n = int(sys.stdin.readline())
people = list(map(int, sys.stdin.readline().split()))

people.sort()

res = 0
count = 0

for val in people:
    count += 1
    if count >= val:
        res += 1
        count = 0

print(res)