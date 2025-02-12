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

    L1 = LII()
    L2 = LII()
    s1 = []
    s2 = []
    for i in range(b):
        if L1[i] == 0:
            s1.append(L2[i])
        else:
            s2.append(L2[i])

    s1.sort(reverse=True)
    s2.sort(reverse=True)
    mi = min(len(s1), len(s2))
    dam = sum(L2)
    for i in range(mi):
        dam += s1[i] + s2[i]
    if len(s1) == len(s2):
        dam -= min(L2)
    print(dam)





