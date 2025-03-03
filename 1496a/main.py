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
    b, c = MII()
    s = I()
    if c == 0:
        print("YES")
        continue

    ok = 1
    for i in range(c):
        ok = ok and s[i] == s[b-i-1]

    if ok and c * 2 < b:
        print("YES")
    else:
        print("NO")
