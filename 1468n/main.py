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
    c1, c2, c3 = MII()
    a1, a2, a3, a4, a5 = MII()

    k = max(0, a4 - (c1 - a1)) + max(0, a5 - (c2 - a2)) + a3
    x = min(c1, a1 + a4)
    y = min(c2, a2 + a5)

    print("YES" if c1 >= a1 and c2 >= a2 and c1 >= x and c2 >= y and c3 >= k else "NO")