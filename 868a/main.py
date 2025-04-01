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
s = I()
a = II()
f = f1 = f2 = False
for _ in range(a):
    s1 = I()
    if s1 == s:
        f = True

    if s1[0] == s[1]:
        f2 = True
    if s1[1] == s[0]:
        f1 = True

print("YES" if (f1 and f2) or f else "NO")