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
L = LII()
K = []
M = []
for i in L:
    if i & 1 == 1:
        K.append(i)
    else:
        M.append(i)

K.sort()
M.sort()
s = abs(len(K) - len(M))
if s <= 1:
    print(0)
else:
    if len(K) > len(M):
        print(sum(K[:len(K) - len(M) - 1]))
    else:
        print(sum(M[:len(M) - len(K) - 1]))