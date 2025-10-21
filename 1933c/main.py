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
t = II()
for _ in range(t):
    a, b, l = MII()

    ans = set()

    for i in range(0, 34):
        x = l
        f = False

        for _ in range(i):
            if x % a:
                f = True
                break
            x //= a

        if f: break

        while True:
            ans.add(x)
            if x % b: break
            x //= b

    print(len(ans))