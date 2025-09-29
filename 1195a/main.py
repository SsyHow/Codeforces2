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
dic = defaultdict(int)
for _ in range(n):
    dic[II()] += 1
L = dic.values()
ans = bad = 0

for i in L:
    if i & 1 == 0:
        ans += i
    else:
        ans += i - 1
        bad += 1

print(ans + (bad + 1) // 2)