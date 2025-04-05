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
h, m = I().split(':')
x = II()
h = int(h)
m = int(m)
hx, mx = x // 60, x % 60

if m + mx >= 60:
    h += 1

m = (m + mx) % 60

h = (h + hx) % 24
k = str(h)
p = str(m)
print('0' * (2 - len(k)) + k + ':' + '0' * (2 - len(p)) + p)

