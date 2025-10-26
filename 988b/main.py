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
L = []
for _ in range(a):
    L.append(I())

L.sort(key = lambda x: len(x))
for i in range(a - 1):
    if L[i] not in L[i + 1]:
        print("NO")
        break
else:
    print("YES")
    print('\n'.join(L))