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
c = ['R', 'W']

for _ in range(t):
    a, b = MII()

    r = [0] * 2
    w = [0] * 2

    for i in range(a):
        s = I()
        for j in range(b):
            if s[j] == 'R':
                r[i+j & 1] = 1
            elif s[j] == 'W':
                w[i+j & 1] = 1

    v = r[1] or w[0]
    vv = r[0] or w[1]

    if v and vv:
        print("NO")
        continue
    print("YES")

    for i in range(a):
        L = []
        for j in range(b):
            L.append(c[i+j+v & 1])
        print(*L, sep='')
