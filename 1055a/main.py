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
L1 = LII()
L2 = LII()

if L1[0] == 0:
    print("NO")
elif L1[b-1] == 1:
    print("YES")

elif L2[b-1] == 1:
    print("YES" if any(L1[i] == L2[i] == 1 for i in range(b, a)) else "NO")
else:
    print("NO")


