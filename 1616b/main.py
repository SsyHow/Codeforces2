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
    s = I()
    f = True
    for i in range(b - 1):
        if f and s[i] > s[i + 1]:
            f = False
        if f and s[i] <= s[i + 1]:
            print(s[:i+1] + s[:i+1][::-1])
            break
        elif not f and s[i] < s[i + 1]:
            print(s[:i + 1] + s[:i + 1][::-1])
            break
    else:
        print(s + s[::-1])