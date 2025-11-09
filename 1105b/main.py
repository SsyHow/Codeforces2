import sys

input = lambda: sys.stdin.readline().rstrip()


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
n, k = MII()
s = I()
dic = {}
ans = 0
cnt = 0

prev = s[0]
for i in range(n):
    if s[i] == prev:
        cnt += 1
    else:
        cnt = 1
        prev = s[i]

    if cnt == k:
        cnt = 0
        dic[s[i]] = dic.get(s[i], 0) + 1
if cnt == k:
    cnt = 0
    dic[s[-1]] = dic.get(s[-1], 0) + 1
print(max(dic.values()) if dic else 0)