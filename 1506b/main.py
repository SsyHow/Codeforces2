
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
    b, c = MII()
    s = list(I())
    i = 0
    while s[i] != '*':
        i += 1
    ans = 0
    while True:
        j = min(b - 1, i + c)
        while i < j and s[j] == '.':
            j -= 1
        if i == j:
            break
        ans += 1
        i = j

    print(ans  +1)