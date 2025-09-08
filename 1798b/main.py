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
    L = []
    b = II()
    for _ in range(b):
        _ = II()
        L.append(LII())

    v = set()
    ans = []
    for i in L[::-1]:
        f = True
        for j in i:
            if f and j not in v:
                ans.append(j)
                f = False
            v.add(j)
        if f == True:
            print(-1)
            break
    else:
        print(*ans[::-1])