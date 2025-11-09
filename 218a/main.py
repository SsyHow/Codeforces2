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
n, k = MII()
L = LII()
for i in range(0, n * 2 + 1, 2):
    if i == 0 and L[i] == L[i + 1]:
        L[i] -= 1
        k -= 1
    elif i == 2 * n and L[i] == L[i - 1]:
        L[i] -= 1
        k -= 1
    elif 0 < i < 2 * n and (L[i] == L[i + 1] or L[i] == L[i - 1]):
        L[i] -= 1
        k -= 1

    if k == 0:
        break

for i in range(1, n * 2 + 1, 2):
    if L[i] > L[i + 1] + 1 and L[i] > L[i - 1] + 1:
        L[i] -= 1
        k -= 1
    if k == 0:
        break
print(*L)