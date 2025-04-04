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

p1, p2 = 0, 0
for i in s:
    if i == 'o':
        p1 += 1
    else:
        p2 += 1
if p1 == 0 or p2 == 0:
    print("YES")
else:
    print("YES" if p2 % p1 == 0 else "NO")