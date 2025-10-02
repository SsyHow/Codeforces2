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
    L = LI()
    ans = 0
    v1 = set()
    v2 = set()
    for i in range(b):
        v2.add(L[i])
        v1.add(L[i])
        if len(v2) == len(v1):
            ans += 1
            v2 = set()

    print(ans)