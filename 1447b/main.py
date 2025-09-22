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
    r, l = MII()
    cnt = 0
    mn = float('inf')
    sm = 0
    z = 0
    for _ in range(r):
        L = LII()
        for i in L:
            if i == 0:
                z += 1
            elif i < 0:
                cnt += 1
                sm += -i
                mn = min(mn, -i)
            else:
                sm += i
                mn = min(mn, i)
    if z == 0 and cnt & 1 == 1:
        print(sm - 2 * mn)
    else:
        print(sm)