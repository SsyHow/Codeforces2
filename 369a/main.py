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
n, m, k = MII()
L = LII()

ans = 0
for i in L:
    if i == 1:
        if m == 0:
            ans += 1
        else:
            m -= 1
    if i == 2:
        if k > 0:
            k -= 1
        elif k == 0 and m > 0:
            m -= 1
        else:
            ans += 1
print(ans)
