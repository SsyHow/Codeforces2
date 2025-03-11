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
def f(k):
    mx, mn = -1, 11
    while k:
        c = k % 10
        mx = max(mx, c)
        mn = min(mn, c)
        k //= 10
    return mx - mn

a = II()
for _ in range(a):
    x, y = MII()
    luc, ans = -1, -1
    for i in range(x, y+1):
        k = f(i)
        if k > luc:
            luc = k
            ans = i
        if luc == 9:
            print(ans)
            break
    else:

        print(ans)