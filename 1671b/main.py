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
    b = II()
    L = LII()

    if L[-1] - L[0] > b + 1:
        print("NO")
        continue
    if b == 1:
        print("YES")
        continue

    for i in range(b - 1):
        if L[i + 1] - L[i] > 3:
            print("NO")
            break
    else:
        print("YES")
