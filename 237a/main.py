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
prevh, prevm = -1, -1
ans = 0
tmp = 1
for _ in range(a):

    h, m = MII()
    if h == prevh and m == prevm:
        tmp += 1

    else:
        tmp = 1
    ans = max(tmp, ans)
    prevh = h
    prevm = m

print(ans)