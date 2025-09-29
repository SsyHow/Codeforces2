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
ans = 0
tmp = 0
cnt = 0
for i in L:
    if i == 1:
        tmp += 1


    else:
        if tmp > 0:
            cnt += 1
            ans += tmp - 1
        tmp = 0
if tmp > 0:
    cnt += 1
    ans += tmp - 1

print(ans + cnt * 2 - 1 if sum(L) != 0 else 0)