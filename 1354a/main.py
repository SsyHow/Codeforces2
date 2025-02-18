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

t = II()
for _ in range(t):
    a, b, c, d = MII()

    k = a - b
    rest = c - d
    ans = b

    if k <= 0:

        print(ans)
        continue
    if rest <= 0:
        print(-1)
        continue

    ans += (k + rest -1)// rest * c
    print(ans)