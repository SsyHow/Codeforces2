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
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n, k = MII()
s = list(I())
dic = defaultdict(list)
for idx, i in enumerate(s):
    dic[i].append(idx)
x = 0
for i in sorted(dic):
    for j in dic[i]:
        if x == k:
            break

        s[j] = ''
        x += 1
if s:
    print(''.join(s))