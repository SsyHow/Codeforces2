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
x, y = MII()
m, n = MII()
p, q = MII()

if 1 <= m <= x and 1 <= n <= y and 1 <= p <= x and 1 <= q <= y:
    print("YES")
elif 1 <= m <= x and y <= n <= a and 1 <= p <= x and y <= q <= a:
    print("YES")
elif x <= m <= a and 1 <= n <= y and x <= p <= a and 1 <= q <= y:
    print("YES")
elif x <= m <= a and y <= n <= a and x <= p <= a and y <= q <= a:
    print("YES")
else:
    print("NO")