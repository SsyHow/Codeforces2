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
    n, m = MII()
    L = []
    x = [0] * m
    for i in range(n):
        k = LII()[1:]
        L.append(k)

        for i in k:
            x[i - 1] += 1
    if any(i == 0 for i in x):
        print("NO")
        continue
    cnt = 0
    for row in L:
        if all(x[i - 1] > 1 for i in row):
            cnt += 1

        if cnt == 2:
            print("YES")
            break
    else:
        print("NO")