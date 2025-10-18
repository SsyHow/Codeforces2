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
n, m = MII()
ans = 0
for i in range(1, 6):
    a = (n - i) // 5 + 1
    b = (m - (5 - i)) // 5 + 1 if i != 5 else (m - (5 - i)) // 5
    # print(a, b)
    ans += a * b
print(ans)
