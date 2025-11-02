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
t = II()
for _ in range(t):
    b = II()
    L = LII()
    s = set(L)
    l, r = 0, b - 1
    k = b
    for i in range(b):
        if L[i] == 0:
            while k in s:
                k -= 1
            L[i] = k
            s.add(k)
    # print(L)
    while l < b and L[l] == l + 1:
        l += 1

    while r > l and L[r] == r + 1:
        r -= 1
    # print(l, r)
    print(r - l + 1 if l != r else 0)