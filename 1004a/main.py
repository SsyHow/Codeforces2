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
L.sort()
b = b * 2
ans = 0
for i in range(1, a):
    if L[i] - L[i - 1] > b:
        ans += 2
    elif L[i] - L[i - 1] == b:
        ans += 1
print(ans+ 2)