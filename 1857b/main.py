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
    s = [0] + [*map(int, list(I()))]
    k = len(s)
    for i in range(k - 1, 0, -1):
        if s[i] > 4:
            s[i - 1] += 1
            k = i
    if s[0] != 0:
        print(s[0], end = '')
    s = [*map(str, s)]

    print(''.join(s[1:k] + ['0'] * (len(s) - k)))