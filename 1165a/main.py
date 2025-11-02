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
n, x, y = MII()
s = I()
ans = 0
s = s[::-1]
for i in range(n):
    if i < x and i != y and s[i] == '1':
        ans += 1
    if i == y and s[i] != '1':
        ans += 1
    if i >= x:
        break
print(ans)