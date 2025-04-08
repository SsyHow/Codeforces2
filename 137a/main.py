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
s = I()

prev = 'X'

ans = 0

k = len(s)
p0 = tmp = 0
while p0 < k:
    if s[p0] != prev:
        ans += 1
        prev = s[p0]
        tmp = 0

    else:
        tmp += 1
        if tmp == 5:
            ans += 1
            tmp = 0

    p0 += 1


print(ans)
