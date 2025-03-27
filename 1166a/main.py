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

from collections import defaultdict
a = II()
vis = set()
ans = 0
k = defaultdict(int)
for _ in range(a):
    b = I()[0]
    k[b] += 1

for _, v in k.items():
    l = v // 2
    m = v - l

    ans += l*(l-1) // 2 + m*(m - 1) //2
print(ans)