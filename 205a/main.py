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
cnt = 0
minx = float('inf')
for i, x in enumerate(L):
    if x < minx:
        minx = x
        cnt = 1
        k = i
    elif x == minx:
        cnt += 1

if cnt >= 2:
    print("Still Rozdil")
else:
    print(k+1)
