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
s = I()
k = len(s)
n = II()

if k % n == 0:

    for i in range(0, k, k//n):
        x = s[i:i + k//n]
        if x != x[::-1]:
            print("NO")
            break
    else:
        print("YES")
else:
    print("NO")
