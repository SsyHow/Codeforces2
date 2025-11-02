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
    n, k = MII()
    L = LII()
    if  k & 1 == 0:

        y = k // 2
        M = []
        cnt = 0
        for i in L:
            if i > y:
                M.append(1)
            elif i < y:
                M.append(0)
            else:
                M.append(1 if cnt & 1 == 1 else 0)
                cnt += 1
        print(*M)
    else:
        y = k // 2
        M = []
        for i in L:
            if i > y:
                M.append(1)
            elif i <= y:
                M.append(0)

        print(*M)
