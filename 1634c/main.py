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
for _ in range(a):
    x, y = MII()
    if y == 1:
        print("YES")
        for i in range(1, x + 1):
            print(i)
        continue
    if x & 1 == 1:
        print("NO")
        continue

    print("YES")
    for i in range(1, x + 1):
        print(*[i for i in range(i, x * y + 1, x)])