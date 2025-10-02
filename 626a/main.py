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

k = defaultdict(int)
ans = 0
x, y = 0, 0
k[(x, y)] += 1
for i in s:
    if i == 'U':
        y += 1
    elif i == 'D':
        y -= 1
    elif i == 'R':
        x += 1
    elif i == 'L':
        x -= 1
    ans += k[(x, y)]
    k[(x , y)] += 1
print(ans)
