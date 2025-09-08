def I():
    return input()


def II():
    return int(input())


def MII(k):
    return map(int, input().split(k))


def LI():
    return list(input().split())


def LII():
    return list(map(int, input().split()))

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
h1, m1 = MII(':')
h2, m2 = MII(':')

k = m2 - m1 + 60 * (h2 - h1)
k //= 2

a = 0
if m1 + k >= 60:
    a = (m1 + k) // 60

print(str(h1 + a).zfill(2), ':', str((m1 + k)%60).zfill(2), sep = '')
