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

pl = pr = b - 1
ans = 0
while pl >= 0 and pr < a:
    if L[pl] == 1 and L[pr] == 1:
        if pl != pr:
            ans += 2
        else:
            ans += 1
    pl -= 1
    pr += 1

if pl > 0:
    ans += sum(L[:pl+1])
elif pr < a:
    ans += sum(L[pr:a])
print(ans)