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
for _ in range(a):
    b = II()
    L = LII()
    L.sort()
    if b > 1:

        x = min(abs(L[i - 1] - L[i]) if L[i] <= 0 else 1 << 60 for i in range(1, b))
        ans = cnt = pos = 0
        for i in L:

            if i < 0 :
                ans += 1
            elif i == 0:
                cnt += 1
            elif i <= x:
                pos += 1
                break
            else:
                break
        # print(cnt, pos, )
        print(ans + max(cnt, pos + min(1, cnt)))
    else:
        print(1)