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
k = 8 - b
ans = 1
if a == 2:
    day = 28
elif a in {1,3,5,7,8, 10, 12}:
    day = 31
else:
    day = 30
while k < day:
    ans += 1
    k += 7
print(ans)