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
    L = LII()
    M = []
    M.append(L[0] - 0)
    for i in range(1, b):
        M.append(L[i] - L[i-1])
    M.append(1440 - L[-1])

    flag = False
    subflag = False
    for i in M:
        if i >= 240:
            flag = True
        elif i >= 120:
            if subflag:
                flag = True
            subflag = True
    print("YES" if flag else "NO")