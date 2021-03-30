import sys

n = int(sys.stdin.readline())
res = 0

for hour in range(n+1):
    for minute in range(60):
        for second in range(60):
            if '3' in str(hour) + str(minute) + str(second):
                res += 1

print(res)