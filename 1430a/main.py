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
def solve(b):
    for i in range(b // 7 + 1):
        for j in range(b//5 + 1):
            for m in range(b//3 + 1):
                if i * 7 + j * 5 + m * 3 == b:
                    return m, j, i
    return (-1, )
a = II()
for _ in range(a):
    b = II()
    k = solve(b)
    print(*k)