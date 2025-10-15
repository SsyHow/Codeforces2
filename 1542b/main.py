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
t = II()
for _ in range(t):
    n, a, b = MII()
    x = 0
    if a == 1:
        print("YES" if (n - 1) % b == 0 else "NO")

        continue
    while a ** x <= n:
        if (n - a ** x) % b == 0:
            print("YES")
            break
        x += 1
    else:
        print("NO")