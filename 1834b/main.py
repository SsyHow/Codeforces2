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
for i in range(a):
    s, t = LI()
    x = max(len(s), len(t))
    s = s.zfill(x)
    t = t.zfill(x)
    idx = 0
    f = True
    ans = 0

    while idx < x:
        if f and s[idx] == t[idx]:
            idx += 1
            continue
        if f and s[idx] != t[idx]:
            ans += abs(int(s[idx]) - int(t[idx]))

            f = False
        else:
            ans += 9
        idx += 1

    print(ans)
