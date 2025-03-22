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
    n, a, b = MII()
    s = I() * 1000
    x, y = 0, 0
    dic = {'N' : (0, 1), 'S': (0, -1), 'E': (1, 0), 'W' :(-1, 0)}
    for i in s:
        x += dic[i][0]
        y += dic[i][1]
        if (x, y) == (a, b):
            print("YES")
            break
    else:
        print("NO")


