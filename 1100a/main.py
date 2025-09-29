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
a, b = MII()
L = LII()
dic1 = defaultdict(int)
dic2 = defaultdict(int)
dic = {1: 0, -1: 0}
for i in range(len(L)):
    if L[i] == 1:
        dic1[i%b] += 1
        dic[1] += 1
    else:
        dic2[i%b] += 1
        dic[-1] += 1
ans = 0
for i in range(b):
    ans = max(abs(dic[1] - dic1[i] - dic[-1] + dic2[i]), ans)
print(ans)