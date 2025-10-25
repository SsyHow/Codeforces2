
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
    s = I()
    L = [0]
    for i in range(len(s)):
        if s[i] == 'R':
            L.append(i + 1)
    L.append(len(s) + 1)


    ans = 0
    for i in range(len(L) - 1):
        ans = max(ans, L[i + 1] - L[i])
    print(ans)