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

def divx(s):
    L = []
    prev = s[0]
    tmp = 0
    for i in s:
        if i == prev:
            tmp += 1
        else:
            L.append(tmp)
            tmp = 1
            prev = i
    if tmp >= 1:
        L.append(tmp)
    return L

t = II()
for _ in range(t):
    p = I()
    s = I()
    L = divx(p)
    M = divx(s)
    n = len(L)
    if len(L) != len(M) or p[0] != s[0]:
        print("NO")
    else:
        print("YES" if all(L[i] <= M[i] <= 2 * L[i] for i in range(n)) else "NO")