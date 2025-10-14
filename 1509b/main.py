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
    b = II()
    s = I()

    x = y = 0
    f = True
    if s.count('M') * 2 != s.count('T'):
        f = False
    if f:
        for i in s:
            if i == 'T':
                x += 1
            elif i == 'M':
                y += 1
                if y > x:
                    f = False
                    break

    if f:
        x = y = 0
        for i in s[::-1]:
            if i == 'T':
                x += 1
            elif i == 'M':
                y += 1
                if y > x:
                    f = False
                    break
    print("NO" if not f else "YES")