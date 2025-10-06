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
    n, k = MII()
    L = []
    for _ in range(n):
        x, y = MII()
        L.append((x, y))

    for i in range(n):
        for j in range(n):
            x, y = L[i]
            p, q = L[j]
            # print(abs(x - p), abs(q - y), k)
            if abs(x - p) + abs(q - y) > k:
                break
        else:
            print(1)
            break
    else:
        print(-1)
