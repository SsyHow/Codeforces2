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
for i in range(a):
    if L[i] == 1:
        ans += 1
    elif 0 < i < a - 1 and L[i-1] == 1 and L[i + 1] == 1:
        ans += 1
    # print(ans)
print(ans)