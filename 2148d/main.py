import sys

input = lambda: sys.stdin.readline().rstrip()


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
t = II()
for _ in range(t):
    b = II()
    L = LII()

    K = []
    ans = 0
    for i in L:
        if i & 1 == 1:
            K.append(i)
        else:
            ans += i

    if len(K) > 0:
        K.sort(reverse=True)
        print(ans + sum(K[:(len(K) + 1) // 2]))
    else:
        print(0)