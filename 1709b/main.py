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
L = LII()
fL = [0] + [max(0, L[i] - L[i+1]) for i in range(a - 1)]
bL = [0] + [max(0, L[i+1] - L[i]) for i in range(a - 1)]
# print(fL)
for i in range(a-1):
    fL[i+1] += fL[i]
    bL[i+1] += bL[i]

for _ in range(b):
    s, t = MII()
    if s < t:
        print(fL[t - 1] - fL[s - 1])
    else:

        print(bL[s - 1] - bL[t - 1])
