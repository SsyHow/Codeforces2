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
    n, c = MII()
    L = LII()
    pow = 4 * n
    cof = sum(L) * 4
    k = sum(i ** 2 for i in L)
    l = 0
    r = 10 ** 9 + 1

    while l <= r:
        mid = (l + r) // 2
        tmp = mid * mid * pow + cof * mid + k
        # print(tmp)
        if tmp == c:
            print(mid)
            break
        elif tmp < c:
            l = mid + 1
        else:
            r = mid - 1

