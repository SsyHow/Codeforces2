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
    ans = 0
    dic = {}
    for i in L:
        dic[i] = dic.get(i, 0) + 1

    k = sorted(dic.values())

    x = len(k)
    for i in range(x):
        # print(i, b, k[i])
        ans = max(ans, (x - i) * k[i])
    print(ans)