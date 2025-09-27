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
from math import gcd
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
L1 = LII()
L2 = LII()
k = 0
def check(m, n):
    if ((m > 0) and (n > 0)) or ((m < 0) and (n < 0)):
        return 1

    return 0
dic = defaultdict(int)
mx = 0
for i in range(a):
    if L1[i] == L2[i] == 0:
        k += 1
    elif L1[i] == 0:
        continue
    else:
        x = gcd(L2[i], L1[i])
        dic[abs(L2[i]) //x , abs(L1[i]) //x , check(L1[i], L2[i])] += 1
        mx = max(mx, dic[abs(L2[i]) //x , abs(L1[i]) //x , check(L1[i], L2[i])])
print(mx + k)