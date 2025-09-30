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
if a == 1:
    print(1)
    print(1)
else:
    ans = 0
    L = []
    while a >= ans + 1:
        L.append(ans + 1)
        ans += 1
        a -= ans
    L[-1] = L[-1] + a
    print(ans)
    print(*L)