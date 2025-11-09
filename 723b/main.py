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

# alpha = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
n = II()
s = I()
s = '_' + s + '_'
ans = 0
cnt = 0
tmp = []
f = False
for i in s:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        tmp.append(i)
    elif i == '(':
        f = True
        ans = max(len(tmp), ans)
        tmp = []
    elif i == ')':
        f = False
        if len(tmp) > 0:
            cnt += 1
        tmp = []
    else:
        if not f:
            ans = max(len(tmp), ans)
            tmp = []
        else:
            if len(tmp) > 0:
                cnt += 1
            tmp = []
print(ans, cnt)