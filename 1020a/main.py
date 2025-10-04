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
n, h, a, b, k = MII()

for _ in range(k):
    ta, fa, tb, fb = MII()
    if ta == tb and fa == fb:
        print(0)
        continue
    ans = 0
    ans += abs(ta - tb)
    if ta != tb:
        if fa < a and fb < a:
            ans += a - fa
            ans += a - fb

        elif fa > b and fb > b:
            ans += fa - b
            ans += fb - b
        else:
            ans += abs(fb - fa)
    else:
        ans += abs(fb - fa)
    print(ans)