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
a = II()
for _ in range(a):
    b = II()
    s = ['0'] + list(I())
    L = [0] + LII()

    ans = 0
    i = 0
    while i <= b:
        mn = L[i]
        sm = L[i]

        j = i + 1
        while j <= b and s[j] == '1':
            mn = min(mn, L[j])
            sm += L[j]
            j += 1
        ans += sm - mn
        i = j
    print(ans)