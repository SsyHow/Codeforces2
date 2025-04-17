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

def getr(n):
    while n & 1 == 0:
        n >>= 1
    return n

a = II()
for _ in range(a):
    b, c = MII()
    if getr(b) != getr(c):
        print(-1)
        continue
    if c > b:
        b, c = c, b
    ans = 0

    k = b // c
    while k >= 8 :
        k //= 8
        ans += 1
    if k > 1:
        ans += 1
    print(ans)
