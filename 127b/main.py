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
L = LII()

dic = defaultdict(int)
for i in L:
    dic[i] += 1
ans = 0
k = 0
for i in dic:

    ans += dic[i] // 4
    if dic[i] % 4 >= 2:
        if k == 0:
            k += 1
        elif k == 1:
            ans += 1
            k = 0
print(ans)


