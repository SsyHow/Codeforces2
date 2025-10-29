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
    a = II()
    L = LII()
    ok = False
    for i in range(1, a-1):
        for j in range(i + 1, a):
            x, y, z = sum(L[:i]), sum(L[i:j]), sum(L[j:])
            # print(x, y, z)
            if x % 3 == y % 3 == z % 3 or {0, 1, 2} == set({x % 3, y % 3, z % 3}):
                print(i, j)
                ok = True
                break
        if ok:
            break

    else:
        print(0, 0)