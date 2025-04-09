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
    x, y = MII()
    L = list(I())

    tmp = L[:y].count('W')
    ans = tmp
    for i in range(y, x):
        if L[i] == 'W':
            tmp += 1
        if L[i-y] == 'W':
            tmp -= 1
        ans = min(ans, tmp)
    print(ans)