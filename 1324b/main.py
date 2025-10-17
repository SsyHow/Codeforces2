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

    dic = {}
    dic2 = {}
    for idx, i in enumerate(L):
        if i not in dic:
            dic[i] = idx
        else:
            dic2[i] = idx
        if i in dic2 and dic2[i] - dic[i] >= 2:
            print("YES")
            break
    else:
        print("NO")

