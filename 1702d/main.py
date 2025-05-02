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

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

a = II()
for _ in range(a):
    s = list(I())
    k = II()
    order = list(zip(s, range(len(s))))
    order.sort()

    x = sum([ord(i) - ord('a') + 1 for i in s])

    while x > k:
        j, i = order.pop()
        s[i] = ''
        x -= ord(j) - ord('a') + 1
    print(''.join(s))
