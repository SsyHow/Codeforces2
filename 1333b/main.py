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
a = II()
for _ in range(a):
    b = II()
    L1 = LII()
    L2 = LII()

    p = n = 0

    for i in range(b - 1, -1, -1):

        if L1[i] > 0 :
            p = 0
        elif L1[i] < 0:
            n = 0

        if L1[i] > L2[i]:
            n += 1

        elif L1[i] < L2[i]:
            p += 1
    # print(p, n)
    print("YES" if p == n == 0 else "NO")
