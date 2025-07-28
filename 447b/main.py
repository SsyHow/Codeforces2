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
s = I()
k = II()
L = LII()
ans = 0
x = 1
for i in s:
    ans +=  x * L[ord(i) - ord('a')]
    x += 1
for i in range(x, x + k ):
    ans += x * max(L)
    x += 1
print(ans)