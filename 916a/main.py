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
    while k:
        if k % 10 == 7:
            return False
        k //= 10
    return True


a = II()
h, m = LII()
ans = 0
hrx = a // 60
tmp = a % 60
while f(h) and f(m):

    if tmp > m:
        h -= 1
    m = (m - tmp) % 60
    h = (h - hrx) % 24
    ans += 1
print(ans)