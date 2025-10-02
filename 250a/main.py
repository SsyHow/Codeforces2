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

tmp = 0
k = 0
ans = 0
M = []
for i in L:

    if i < 0 :
        tmp += 1
        if tmp == 3:
            ans += 1
            M.append(k)
            tmp = 1
            k = 0
    k += 1
M.append(k)
ans += 1
print(ans)
print(*M)