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
    n = II()
    ans = [0, 0, 0, 0]

    f = 1
    for i in range(1, 20000):
        who = 0 if i % 4 == 1 or i % 4 == 0 else 1
        cnt = i
        if n < cnt:
            cnt = n
        cntw = (cnt + f % 2) // 2
        cntb = cnt - cntw

        ans[who * 2 + 0] += cntw
        ans[who * 2 + 1] += cntb

        f += cnt
        n -= cnt
        if n == 0:
            break
    print(*ans)