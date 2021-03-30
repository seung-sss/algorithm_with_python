import sys

def prime(n):
    sieve = [True] * (n+1)
    tmp = int(n**0.5)

    for i in range(2, tmp+1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False

    return [i for i in range(2, n+1) if sieve[i] == True]

while True:
    tmp = int(sys.stdin.readline())

    if tmp == 0:
        break
    else:
        p = prime(tmp * 2)
        cnt = 0
        for val in p:
            if tmp < val:
                cnt += 1
        print(cnt)
