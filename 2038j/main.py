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
p = 0
for _ in range(a):
    x, y = I().split()
    y = int(y)
    if x == 'P':
        p += y

    else:

        if p - y < 0:
            print("YES")
        else:
            print("NO")
        p = max(0, p - y)