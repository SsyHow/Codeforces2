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
k1 = set()
k2 = set()

for i in L:
    if i not in k1:
        k1.add(i)
    elif i not in k2:
        k2.add(i)
    else:
        print("NO")
        break
else:
    print("YES")
    print(len(k1))
    print(*sorted(k1))
    print(len(k2))
    print(*sorted(k2, reverse = True))
