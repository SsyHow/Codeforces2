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

l, r = I().split('^')

l = l[::-1]
la = ra = 0
for idx, i in enumerate(l, start=1):
    if '0' <= i <= '9':
        la += idx * int(i)

for idx, i in enumerate(r, start=1):
    if '0' <= i <= '9':
        ra += idx * int(i)

if la == ra:
    print("balance")
elif la > ra:
    print("left")
else:
    print("right")
