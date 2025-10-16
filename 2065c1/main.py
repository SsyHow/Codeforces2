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
for _ in range(II()):
    b, c = MII()
    L = LII()
    x = II()

    prev = float('-inf')

    for i in range(b):
        m, n = L[i], x - L[i]
        if max(m, n) < prev:
            print("NO")
            break
        elif min(m, n) > prev:
            prev = min(m, n)
        elif m > prev and n < prev:
            prev = m
        elif n > prev and m < prev:
            prev = n
    else:
        print("YES")