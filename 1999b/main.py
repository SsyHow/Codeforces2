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
    a1, a2, b1, b2 = MII()
    ans = 0
    if (a1 > b1 and a2 >= b2) or (a1 >= b1 and a2 > b2):
        ans += 1
    if (a1 > b2 and a2 >= b1) or (a1 >= b2 and a2 > b1):
        ans += 1
    if (a2 > b1 and a1 >= b2) or (a2 >= b1 and a1 > b2):
        ans += 1
    if (a2 > b2 and a1 >= b1) or (a2 >= b2 and a1 > b1):
        ans += 1
    print(ans)