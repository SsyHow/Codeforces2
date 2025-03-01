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
    cnt = 0
    for i in s:
        if i != '?':
            cnt += 1
    s = list(s)
    if not cnt:
        s[0] = 'R'

    for i in range(1, b):
        if s[i] == '?' and s[i-1] != '?':
            s[i] = 'R' if s[i-1] == 'B' else 'B'

    for i in range(b-2, -1, -1):
        if s[i] == '?' and s[i+1] != "?":
            s[i] = 'R' if s[i+1] == 'B' else 'B'

    print(''.join(s))
