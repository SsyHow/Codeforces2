import sys

input = sys.stdin.readline


def I():
    return input().strip()


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
    s = list(I())
    t = I()
    k = len(t)
    j = 0
    for i in range(len(s)):
        if s[i] == '?':
            if j < k:
                s[i] = t[j]
                j += 1
            else:
                s[i] = t[j - 1]

        elif j < k and s[i] == t[j]:
            j += 1

    if j == k:
        print("YES")
        print("".join(s))
    else:
        print("NO")