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
    m, n = MII()
    flag = False
    if x == m and y + n == x:
        flag = True
    elif x == n and y + m == x:
        flag = True
    elif y == m and x + n  == y:
        flag = True
    elif y == n and x + m == y:
        flag = True

    print("YES" if flag else "NO")
