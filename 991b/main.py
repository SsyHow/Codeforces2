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
L = LII()
L.sort()
k = sum(L)
ans = 0
if k / a >= 4.5:
    print(0)
else:

    for i in L:
        k += 5 - i
        ans += 1
        if k / a >= 4.5:
            print(ans)
            break

