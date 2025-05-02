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
    n, m = MII()

    L = []
    for _ in range(n):
        L.append(LII())

    ans = []
    for x in L:
        v = set(i%n for i in x)
        if len(v) > 1:
            print(-1)
            break
        ans.append(list(v)[0])
    else:
        print(*[i[1] for i in sorted(zip(ans, range(1, n + 1)))])