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
    s = I()
    for _ in range(c):
        m, n = MII()
        m -= 1
        n -= 1
        bad = True
        i = 0
        while i < m and bad:
            if (s[i] == s[m]):
                bad = False
            i+=1
        i = n + 1
        while i < b and bad:
            if s[i] == s[n]:
                bad = False
            i += 1
        print("NO" if bad else "YES")
