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
cur = (float('-inf'), 'y')
for _ in range(t):
    name, p, m, a, b, c, d, e = I().split()
    p = int(p)
    m = int(m)
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)

    k = a + b + c + d + e + p * 100 - m *  50
    if k > cur[0]:
        cur = (k, name)

print(cur[1])