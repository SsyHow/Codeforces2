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

L1 = LII()
L2 = LII()
p1 = p2 = 0
for i in range(a):
    if L1[i] > L2[i]:
        p1 += 1
    elif L2[i] > L1[i]:
        p2 += 1

if p1 == 0:
    print(-1)
else:
    print(p2 // p1 + 1)