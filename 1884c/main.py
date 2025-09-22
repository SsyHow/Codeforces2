def I():
    return input()


def II():
    return int(input())


def MII():
    return map(int, input().split())


def LI():
    return list(input().split())


def LII():
    return list(map(int, input().split()))
from collections import defaultdict
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def foo(x, m, n, L):
    if m == x or x == n:
        return
    L[m - 1] += 1
    L[n] -= 1
def calc(L):
    ans = 0
    k = 0
    for i in sorted(L):
        k += L[i]
        ans = max(ans, k)
    return ans
a = II()

for _ in range(a):
    x, y = MII()
    s = defaultdict(int)
    e = defaultdict(int)

    for i in range(x):
        m, n = MII()
        foo(1, m, n, s)
        foo(y, m, n, e)
    print( max(calc(s),calc(e)))


