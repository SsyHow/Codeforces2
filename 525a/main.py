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
from collections import defaultdict
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
s = I()
dic = defaultdict(int)
ans = 0
for i in range((a - 1) * 2):
    if i & 1 == 0:
        dic[s[i].upper()] += 1
    else:
        if dic[s[i]] == 0:
            ans += 1
        else:
            dic[s[i]] = max(0, dic[s[i]] - 1)
print(ans)