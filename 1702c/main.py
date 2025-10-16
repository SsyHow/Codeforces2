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
res = []
for _ in range(a):
    # _ = I()
    _ = I()
    n, k = MII()
    L = LI()
    dic1 = {}
    dic2 = {}
    for i in range(n):
        if L[i] not in dic1:
            dic1[L[i]] = i
        dic2[L[i]] = i
    for i in range(k):
        x, y = LI()
        if x in dic1 and y in dic2 and dic1[x] < dic2[y]:
            res.append("YES")
        else:
            res.append("NO")

print('\n'.join(res))