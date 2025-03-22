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
    x, y = MII()
    L = []
    for _ in range(x):
        L.append(list(I()))
    ans = []

    for j in range(y):
        tmp = []
        s = p = 0
        for i in range(x):
            if L[i][j] == 'o':
                for _ in range(p):
                    tmp.append('.')
                p = 0
                for _ in range(s):
                    tmp.append('*')
                s = 0
                tmp.append('o')

            elif L[i][j] == '*':
                s += 1
            elif L[i][j] == '.':
                p += 1

        for _ in range(p):
            tmp.append('.')
        for _ in range(s):
            tmp.append('*')
        ans.append(tmp)

    k = list(zip(*ans))
    for i in k:
        print(*i, sep='')

