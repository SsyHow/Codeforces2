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
    r, g, b, w = MII()
    if (((r & 1) + (g & 1) + (b & 1) + (w & 1)) <= 1):
        print("YES")
    elif (r > 0 and g > 0 and b > 0 and (((r - 1) & 1) + ((g - 1) & 1) + ((b - 1) & 1) + ((w + 3) & 1)) <= 1):
        print("YES")
    else:
        print("NO")