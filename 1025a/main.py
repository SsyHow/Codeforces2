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
a = II()
s = I()
from collections import defaultdict
k = defaultdict(int)
if a != 1:
    for i in s:
        k[i] += 1
        if k[i] == 2:
            print("YES")
            break
    else:
        print("NO")
else:
    print("YES")