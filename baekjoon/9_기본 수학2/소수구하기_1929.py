import sys

def prime(n):
    sieve = [True] * (n+1)
    tmp = int(n ** 0.5)

    for i in range(2, tmp+1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False

    return [i for i in range(2, n+1) if sieve[i] == True]

m, n = map(int, sys.stdin.readline().split())
prime_list = prime(n)

for val in prime_list:
    if val >= m:
        print(val)

