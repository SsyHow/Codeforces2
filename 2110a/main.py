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
    L = LII()
    L.sort()

    if L[0] & 1 == L[-1] & 1:
        print(0)
        continue
    l, r = L[0] & 1, L[-1] & 1
    x = 1
    while x < b and r != L[x] & 1 and l != L[b - 1 - x] & 1:
        # print(L[x] & 1, L[b - 1 - x])
        x += 1
    print(x )
