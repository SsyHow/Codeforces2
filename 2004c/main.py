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
    n, k = MII()
    L = LII()
    L.sort(reverse=True)

    x = L[-1]
    y = n
    if n & 1 == 1:
        n -= 1
    ans = 0
    for i in range(0, n, 2):
        tmp = L[i] - L[i + 1]
        if k > 0:
            if k >= tmp:
                k -= tmp
            else:

                ans += tmp - k
                k = 0
        else:
            ans += tmp
    print(ans if y & 1 == 0 else ans + x)