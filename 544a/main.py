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
L = list(I())

ans = []
tmp = []
i = 0
vis = set()
while len(ans) < a - 1 and i < len(L):
    tmp.append(L[i])
    vis.add(L[i])
    i += 1

    while i < len(L) and L[i] in vis:
        tmp.append(L[i])
        vis.add(L[i])
        i += 1
    ans.append(''.join(tmp))
    tmp = []
if i < len(L):
    print("YES")
    ans.append(''.join(L[i:]))
    print('\n'.join(ans))
else:
    print("NO")
