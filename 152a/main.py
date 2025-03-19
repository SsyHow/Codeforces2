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
n, m = MII()

K = []
for i in range(n):
    K.append(II())
s = set()
while K[0]:
    dx, x = -1, 0
    L = []

    for idx, i in enumerate(K):
        tmp = K[idx] % 10
        K[idx] //= 10
        if tmp > x:
            dx, x = idx, tmp
            L = [dx]
        elif tmp == x:
            L.append(idx)
    # print(L)
    for i in L:
        s.add(i)
print(len(s))