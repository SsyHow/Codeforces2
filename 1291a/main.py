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

def calc(s):

    return sum([int(i) for i in s])

a = II()
for _ in range(a):
    b = II()
    s = I()
    while s and (int(s[-1]) & 1 == 0 or calc(s) & 1 == 1):
        s = s[:-1]

    if s == '':
        print(-1)
    else:
        print(s)


