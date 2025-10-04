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

s = I()
tmp = []
f = True
h = 0
for i in s:
    tmp.append(i)
    if i == '<':
        f = True
    if i == '/':
        f = False

    if i == '>':
        if not f:
            h -= 2
        print(' ' * h,''.join(tmp), sep='')
        if f:
            h += 2
        tmp = []