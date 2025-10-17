import sys

input = sys.stdin.readline


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
    f = False

    i = 0
    j = b - 1
    ans = []
    # tmp = []
    while i <= j:
        if f:
            if L[i] > L[j]:
                ans.append("L")
                # tmp.append(L[i])
                i += 1
            else:
                ans.append("R")
                # tmp.append(L[j])
                j -= 1
        else:
            if L[i] < L[j]:
                ans.append("L")
                # tmp.append(L[i])
                i += 1
            else:
                ans.append("R")
                # tmp.append(L[j])
                j -= 1

        f = not f
    print(''.join(ans))
    # print(tmp)