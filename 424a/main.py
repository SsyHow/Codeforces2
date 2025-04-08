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
from collections import Counter
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
s = list(I())

c = Counter(s)

if c['x'] == c['X']:
    print(0)
    print(''.join(s))
elif c['x'] > c['X']:
    print(a // 2 - c['X'])
    for i in range(a):
        if s[i] == 'x':
            s[i] ='X'
            c['x'] -= 1
            c['X'] += 1
            if c['x'] == c['X']:
                break
    print(''.join(s))
else:

    print(a // 2 - c['x'])
    for i in range(a):
        if s[i] == 'X':
            s[i] = 'x'
            c['X'] -= 1
            c['x'] += 1
            if c['x'] == c['X']:
                break
    print(''.join(s))
