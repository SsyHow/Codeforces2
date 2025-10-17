import sys

input = sys.stdin.readline


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
n, q = MII()
k = [0] * 51
L = LII()
M = LII()

for idx, i in enumerate(L):
    if k[i] == 0:
        k[i] = idx + 1
# print(k)
ans = []
for i in M:
    ans.append(k[i])
    for j in range(51):
        if k[j] < k[i]:
            k[j] += 1
    k[i] = 1
print(*ans)