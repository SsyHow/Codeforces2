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
dic = defaultdict(int)

for _ in range(a):
    dic[II()] += 1
k = list(dic.keys())
if len(dic) != 2 or dic[k[0]] != dic[k[1]]:
    print("NO")
else:
    print("YES")
    print(*k)
