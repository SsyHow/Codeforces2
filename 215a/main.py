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
n = II()
L = LII()
m = II()
M = LII()
k = 0
ans = 0
for i in M:
    for j in L:
        if i % j == 0:
            tmp = i // j
            if tmp == k:
                ans += 1
            elif tmp > k:
                ans = 1
                k = tmp
print(ans)