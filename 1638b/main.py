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
    L = LII()
    lco = 1
    lce = 0

    for i in L:
        if i & 1 == 1:
            if i < lco:
                print("NO")
                break
            else:
                lco = max(i, lco)
        else:
            if i < lce:
                print("NO")
                break
            else:
                lce = max(i, lce)

    else:
        print("YES")
