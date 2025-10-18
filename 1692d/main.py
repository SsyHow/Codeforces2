import sys

input = sys.stdin.readline


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
    t, mins = LI()

    hh, mm = map(int, t.split(':'))
    vis = set()
    ans = 0
    mins = int(mins)
    while (hh, mm) not in vis:
        vis.add((hh, mm))
        mm += mins
        a = mm // 60
        mm %= 60

        hh += a
        hh %= 24
        if str(hh).zfill(2) == str(mm).zfill(2)[::-1]:
            ans += 1
    # print(vis)
    print(ans)
