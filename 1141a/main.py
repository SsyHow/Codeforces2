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
a, b = MII()
if (b % a) > 0:
    print(-1)
else:
    ans = 0
    k = b // a

    while k % 6 == 0:
        ans += 2
        k //= 6
    while k % 3 == 0:
        ans += 1
        k //= 3
    while k % 2 == 0:
        ans += 1
        k //= 2
    print(ans if k == 1 else -1)