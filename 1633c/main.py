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
    hc, dc = MII()
    hm, dm = MII()

    k, w, a = MII()



    for i in range(k + 1):
        att = dc + w * i
        hea = hc + a * (k - i)

        if (hm + att - 1) // att <= (hea + dm - 1) // dm:
            print("YES")
            break

    else:
        print("NO")