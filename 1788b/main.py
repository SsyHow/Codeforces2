import sys

input = lambda: sys.stdin.readline().rstrip()


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
def cc(x):
    ans = 0
    for i in x:
        ans *= 10
        ans += i
    return ans

for _ in range(a):
    b = II()
    if b & 1 == 1:
        x = []
        y = []
        b = str(b)
        f = -1
        for i in b:
            i = int(i)
            if i & 1 == 0:
                x.append(i // 2)
                y.append(i // 2)
            else:

                x.append((i - 1 * f) // 2)
                y.append((i + 1 * f) // 2)
                f = -f
        print(cc(x), ' ', cc(y),  sep = '')
    else:
        print(b // 2, b // 2)