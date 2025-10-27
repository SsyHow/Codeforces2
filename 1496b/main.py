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
def mex(L):
    for i in range(len(L)):
        if i not in L:
            return i
    return len(L)
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def mex(L):
    for i in range(len(L)):
        if i not in L:
            return i
    return len(L)

t = II()
for _ in range(t):
    n, k = MII()
    L = set(MII())

    if mex(L) == n:
        print(n + k)
    # elif mex(L) == 0:
    #     print(n)

    else:
        while k:
            a = max(L)
            b = mex(L)
            x = len(L)
            L.add((a + b + 1) // 2)
            if x == len(L):
                print(x)
                break
            k -= 1
        else:
            print(len(L))