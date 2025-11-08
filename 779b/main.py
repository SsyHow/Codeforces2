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

n, k = LI()
k = int(k)
ans = 0
for i in range(len(n) - 1, -1, -1):
    if n[i] == '0':
        k -= 1
    else:
        ans += 1
    if k == 0:
        print(ans)
        break
else:
    print(len(n) - 1)