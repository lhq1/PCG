import math


def lpn_security(n, t):
    c1 = 2.8 * math.log2(n)
    c2 = math.log2(math.comb(4 * n, t))
    c3 = math.log2(math.comb(n, t))
    return c1 + c2 - c3


def choose_weight(n, goal, start=10, end = 55):
    for i in range(start, end):
        if lpn_security(n, i) > goal:
            return i
    return 0


def lpn_security_general(n, k, t):
    c1 = 2.8 * math.log2(k)
    c2 = math.log2(math.comb(n, t))
    c3 = math.log2(math.comb(n-k, t))
    return c1 + c2 - c3


def dual_lpn_general(N, n, t):
    k = N - n
    return lpn_security_general(N, k, t)
