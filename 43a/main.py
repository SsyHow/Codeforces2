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
dic = defaultdict(int)
a = II()
for _ in range(a):
    s = I()
    dic[s] += 1


k = list(dic.items())
if len(k) == 1:
    print(k[0][0])
else:
    if k[0][1] > k[1][1]:
        print(k[0][0])
    else:
        print(k[1][0])