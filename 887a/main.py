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
s = '1000000'
t = I()
ps = pt = 0

while ps < len(s) and pt < len(t):
    if s[ps] == t[pt]:
        ps += 1
        pt += 1
    else:
        pt += 1

if ps == len(s):
    print("yes")
else:
    print("no")