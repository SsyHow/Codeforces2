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
    n, m, k = MII()
    s = I()
    x = c = i = 0
    while i < n:
        c = 0 if s[i] != '0' else c + 1
        if c == m:
            x += 1
            c = 0
            i += k - 1
        i += 1
    print(x)