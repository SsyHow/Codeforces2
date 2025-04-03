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
dic = defaultdict(int)
for i in range(4):
    k = list(I())
    for i in k:
        if i in '123456789':
            dic[i] += 1
for i in dic:
    if dic[i] > 2* a:
        print("NO")
        break
else:
    print("YES")