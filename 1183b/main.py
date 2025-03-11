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
for _ in range(II()):
    b, c = MII()
    L = LII()

    k = max(L)
    M = [i + c for i in L]
    x = min(M)
    for i in L:
        # print(i, x, k)
        if abs(i - x) > c:
            print(-1)
            break
    else:
        print(min(M))
