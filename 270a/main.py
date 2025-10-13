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
L = set()
for i in range(361):
    k = 180 * i / (i + 2)
    if int(k) == k:
        L.add(k)

a = II()
# print(L)
for i in range(a):
    b = II()
    if b in L:
        print("YES")
    else:
        print("NO")
