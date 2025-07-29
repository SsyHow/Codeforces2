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
for _ in range(t):
    b = I()
    f = False
    cnt = 0
    for i in range(len(b)-1, -1, -1):
        if f and b[i] != '0':
            cnt += 1

        elif not f and b[i] == '0':
            cnt += 1

        elif b[i] != '0':
            f = True
    print(cnt)