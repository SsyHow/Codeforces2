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
    b = II()
    s = I()

    k = set(range(1, b + 1))
    ans = []
    for i in range(b - 2, -1, -1):
        if s[i] == '<':
            ans.append(min(k))
            k.remove(min(k))
        else:
            ans.append(max(k))
            k.remove(max(k))
    for i in k:
        ans.append(i)
    print(*ans[::-1], sep=' ')