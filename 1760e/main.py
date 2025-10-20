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

def calc(L):
    ans = one = 0
    for i in L:
        if i == 1:
            one += 1
        else:
            ans += one
    return ans


# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
for _ in range(a):
    b = II()
    L = LII()

    ans = calc(L)
    i = 0
    while i < b and L[i] == 1:
        i += 1
    if i < b:
        L[i] = 1
        # print(L)
        ans = max(ans, calc(L))
        L[i] = 0
    # print(L)
    j = b - 1
    while j > - 1 and L[j] == 0:
        j -= 1
    if j > -1:

        L[j] = 0
        # print(L)
        ans = max(ans, calc(L))
    print(ans)
