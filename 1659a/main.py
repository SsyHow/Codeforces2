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
    n, r, b = MII()

    q, rem = divmod(r, b + 1)

    parts = []
    for i in range(b + 1):
        length = q + 1 if i < rem else q
        parts.append('R' * length)
        if i < b:
            parts.append('B')

    print(''.join(parts))

