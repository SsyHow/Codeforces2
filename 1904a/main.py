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
    b, c = MII()
    x1, y1 = MII()
    x2, y2 = MII()

    dir = {(b, c), (-b, c), (b, -c), (-b, -c), (c, b), (-c, b), (c, -b), (-c, -b)}
    k = set()
    ans = 0
    for i in dir:
        k.add((x1+i[0], y1 + i[1]))

    for i in dir:
        if (x2 + i[0], y2+ i[1]) in k:
            ans += 1
    print(ans)