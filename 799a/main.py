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
n, t, k, d = MII()
time1 = ((n + k - 1) // k) * t
time = time1 - 1
cakes = (time // t) * k
if time >= d:
    cakes += ((time - d) // t) * k

if cakes >= n:
    print("YES")
else:
    print("NO")