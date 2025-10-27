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
def check(arr):
    n = len(arr)
    for i in range(n):
        left = arr[i - 1]
        right = arr[(i + 1) % n]
        if not ((arr[i] > left and arr[i] > right) or (arr[i] < left and arr[i] < right)):
            return False
    return True
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
t = II()
for _ in range(t):
    n = II()
    L = LII()
    if n & 1 == 1:
        print("NO")
        continue
    L.sort()
    res = []
    for i in range(n // 2):
        res.append(L[i])
        res.append(L[n // 2 + i])
    if check(res):
        print("YES")
        print(*res)
    else:
        print("NO")