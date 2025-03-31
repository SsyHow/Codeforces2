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
s = I()
x, y = 0, 0
ans = 0
L = []
for i in s:
    if i == 'U':
        x += 1
    else:
        y += 1

    if x == y:
        L.append(0)
    elif x > y:
        L.append(1)
    else:
        L.append(-1)

f = L[0]
for i in L[1:]:
    if i == -f:
        f = -f
        ans += 1
print(ans)