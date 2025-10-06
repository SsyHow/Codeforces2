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

from collections import defaultdict
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n, k = MII()
L = LII()

c = defaultdict(lambda : defaultdict(int))
x = n // k
for i in range(n):
    c[i%k][L[i]] += 1

# print(c)
ans = 0
for i in c:
    ans += sum(c[i].values()) - max(c[i].values())
print(ans)