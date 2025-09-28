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
L = LII()
ans = 0
tmp = 0
for i in L:

    if tmp + i > m:
        ans += 1
        tmp = i
    elif tmp == m:
        ans += 1
        tmp = 0
    else:
        tmp += i

print(ans + 1 if tmp else ans)