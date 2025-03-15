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
n, l, r = MII()
def f(x):
    ans = 0
    for i in range(x):
        ans += 1 << i
    return ans

print(1* (n - l) + f(l), (1 << (r - 1)) * (n - r) + f(r))
