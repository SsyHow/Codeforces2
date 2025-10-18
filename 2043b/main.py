import sys

input = sys.stdin.readline
sys.set_int_max_str_digits(6000)


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
from math import factorial
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
for _ in range(a):
    n, d = MII()
    k = factorial(min(n, 7))

    kk = int(str(d) * k)
    ans = []
    for i in range(1, 10, 2):
        if kk % i == 0:
            ans.append(i)

    print(*ans)