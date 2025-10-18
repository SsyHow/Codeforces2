import sys

input = sys.stdin.readline


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
for _ in range(a):
    b, c = MII()
    L = LII()
    pos = []
    neg = []
    for i in L:
        if i > 0:
            pos.append(i)
        else:
            neg.append(-i)
    pos.sort()
    neg.sort()
    ans = []
    for i in range(len(pos) - 1, -1, -c):
        ans.append(pos[i])
    for j in range(len(neg) - 1, -1, -c):
        ans.append(neg[j])
    ans.sort()
    print(sum(i * 2 for i in ans[:-1]) + ans[-1])



