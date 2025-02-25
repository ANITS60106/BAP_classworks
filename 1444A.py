import math

def factorize(n):
    factors = {}
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
        i += 2
    if n > 1:
        factors[n] = 1
    return factors

def xyi(p, q):
    if p % q != 0:
        return p
    q_factors = factorize(q)
    x = 1
    for prime in q_factors:
        temp = p
        while temp % q == 0:
            temp //= prime
        if temp % q != 0:
            x = max(x, temp)
    return x

t = int(input())
for _ in range(t):
    p, q = map(int, input().split())
    print(xyi(p, q))