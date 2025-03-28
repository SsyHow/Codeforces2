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
mx1, mx2 = sorted(L2[:2], reverse=True)
for i in L2[2:]:
    if i >= mx1:
        mx2 = mx1
        mx1 = i
    elif i > mx2:
        mx2 = i

print("YES" if mx1 + mx2 >= sum(L1) else "NO")