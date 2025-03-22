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
a, b = MII()
L1 = LII()
L2 = LII()
if len(L2) == 1:
    for i in range(a):
        if L1[i] == 0:
            L1[i] = L2[0]
    if L1 == sorted(L1):
        print("NO")
    else:
        print("YES")
else:
    print("YES")

