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
home = I()
dic = defaultdict(int)
for _ in range(a):
    s, t = I().split('->')
    dic[s] += 1
    dic[t] -= 1

for i in dic:
    if dic[i] != 0:
        print("contest")
        break
else:
    print("home")