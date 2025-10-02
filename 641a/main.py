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
L = LII()
vis = set()

i = 0

while 0 <= i < a:
    if i in vis:
        print("INFINITE")
        break
    vis.add(i)
    if s[i] == '>':
        i += L[i]
    elif s[i] == '<':
        i -= L[i]
else:
    print("FINITE")
