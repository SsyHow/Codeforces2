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
L = []
for i in range(a):
    L.append(LII())
def f():
    for i in range(a):
        for j in range(a):
            if L[i][j] != 1:
                flag = False
                for x in range(a):
                    for y in range(a):
                        if L[i][x] + L[y][j] == L[i][j]:
                            flag = True
                            break
                    if flag:
                        break

                if not flag:
                    return 'NO'
    return 'YES'

print(f())
