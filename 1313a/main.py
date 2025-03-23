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
    x, y, z = sorted(MII())
    ans = 0

    if x:
        x -= 1
        ans += 1
    if y:
        y -= 1
        ans += 1
    if z:
        z -= 1
        ans += 1

    if x >= 1 and z >= 1:
        ans += 1
        x -= 1
        z -= 1
    if y >= 1 and z >= 1:
        ans += 1
        y -= 1
        z -= 1
    if x >= 1 and y >= 1:
        ans += 1
        x -= 1
        y -= 1

    if x >= 1 and y >= 1 and z >= 1:
        ans += 1
    print(ans)

