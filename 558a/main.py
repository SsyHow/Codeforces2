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
t = II()
neg = []
pos = []
n = p = 0
for _ in range(t):
    xi, ai = MII()

    if xi < 0:
        neg.append((xi, ai))
        n += 1
    else:
        pos.append((xi, ai))
        p += 1

neg.sort(reverse=True)
pos.sort()
if n == p:
    print(sum(i[1] for i in neg) + sum(i[1] for i in pos))
elif n > p:
    print(sum(i[1] for i in neg[:p + 1]) + sum(i[1] for i in pos))
else:
    print(sum(i[1] for i in neg) + sum(i[1] for i in pos[:n + 1]))

