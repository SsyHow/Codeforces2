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
    k = []
    for i in range(b):
        if s[i] == '2':
            k.append(i)
    if 0 < len(k) <= 2:
        print("NO")
        continue
    ans = [['=' for _ in range(b)] for _ in range(b)]
    for i in range(b):
        ans[i][i] = 'X'

    for idx, i in enumerate(k):
        x, y = i, k[(idx + 1) % len(k)]
        ans[x][y] = '+'
        ans[y][x] = '-'
    print("YES")
    for i in ans:
        print(*i, sep='')


