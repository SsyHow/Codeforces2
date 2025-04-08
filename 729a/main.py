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

m = []

p0 = 0
while p0 < a:
    if s[p0] != 'o':
        m.append(s[p0])
        p0 += 1
        continue

    f = False
    while p0 + 2 < a and s[p0] == 'o' and s[p0 + 1] == 'g' and s[p0 + 2] == 'o':
        p0 += 2
        f = True
    if f:
        m.append('***')
    else:
        m.append(s[p0])
    p0 += 1

print(''.join(m))