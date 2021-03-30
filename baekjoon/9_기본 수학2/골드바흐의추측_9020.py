import sys

def prime(n):
    sieve = [True] * (n+1)
    tmp = int(n**0.5)

    for i in range(2, n+1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False

    return [i for i in range(2, n+1) if sieve[i] == True]

# 아래 함수 부분 참고함( 다시 공부해 보기! )
def sosu(n):
    li = prime(n)
    idx = max([i for i in range(len(li)) if li[i] <= (n/2)])
    for i in range(idx, -1, -1):
        for j in range(i, len(li)):
            if li[i] + li[j] == n:
                return [li[i], li[j]]

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print(" ".join(map(str, sosu(n))))






