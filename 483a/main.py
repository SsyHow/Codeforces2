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
l,r = MII()

if r - l < 2 or (r - l == 2 and l & 1 == 1):
    print(-1)

elif l & 1 == 0:
    print(l, l + 1, l + 2)
else:
    print(l + 1, l + 2, l + 3)