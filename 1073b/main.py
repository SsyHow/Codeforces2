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
L1 = LII()
L2 = LII()
s = set()
L1.reverse()

ans = []

for i in L2:

    tmp = 0
    if i in s:
        ans.append(tmp)
        continue
    while L1 and L1[-1] != i:
        x = L1.pop()
        s.add(x)
        tmp += 1
    x = L1.pop()
    s.add(x)
    tmp += 1

    ans.append(tmp)
print(*ans)
