import sys

input = lambda: sys.stdin.readline().rstrip()


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

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def good(n):
    return n % 2 and n % 3 and n % 5 and n % 7

def get_naive(x):
    ans = 0
    for i in range(x):
        if good(i):
            ans += 1
    return ans

def get(r):
    return (r // 210) * get_naive(210) + get_naive(r % 210)


a = II()
for _ in range(a):
    l, r = MII()
    print(get(r + 1) - get(l))
