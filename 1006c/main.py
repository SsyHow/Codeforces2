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
b = II()
L = LII()

pre = []
suf = []
x = 0
y = sum(L)
for i in L:
    x += i
    pre.append(x)

    suf.append(y)
    y -= i
k = set(suf)
tmp = 0
for i in range(b):
    k.remove(suf[i])
    if pre[i] in k:
        tmp = pre[i]
print(tmp)
