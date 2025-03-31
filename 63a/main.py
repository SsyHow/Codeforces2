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
c = []
w = []
r = []
m = []
for _ in range(a):
    s1, s2 = I().split()
    if s2 == "captain":
        c.append(s1)
    elif s2 == "woman" or s2 == "child":
        w.append(s1)
    elif s2 == "man":
        m.append(s1)
    else:
        r.append(s1)

print(*r, *w, *m, *c, sep='\n')