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
    if L1[-1] != L2[-1]:
        print("NO")
        continue

    for i in range(b - 2, -1, -1):
        if L1[i] != L2[i] and L1[i] ^ L1[i + 1] != L2[i] and L1[i] ^ L2[i + 1] != L2[i]:
                print("NO")
                break
    else:
        print("YES")