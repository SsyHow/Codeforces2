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
L = []
for _ in range(n):
    L.append(LII())
ans = 0

for i in range(1, 101):
    for j in range(1, 101):
        for lis in L:
            if lis[0] <= i <= lis[2] and lis[1] <= j <= lis[3]:
                ans += 1
print(ans)