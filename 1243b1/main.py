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
    t = I()
    L = []
    c = 0
    f = False
    for i in range(b):
        if s[i] == t[i]:
            continue
        c += 1

        if not L:
            L.append(s[i])
            L.append(t[i])

        else:
            if L[0] == s[i] and L[1] == t[i]:
                f = True
            else:
                f = False
    if (c == 2 and f) or c == 0:
        print("YES")
    else:
        print("NO")