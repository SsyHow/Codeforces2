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

a, b = MII()
s = list(I())

last = {}
act = set()

for idx, x in enumerate(s):
    last[x] = idx

for i in range(a):
    act.add(s[i])

    if len(act) > b:
        print("YES")
        break
    if last[s[i]] == i:
        act.remove(s[i])

else:
    print("NO")
