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
def solve():
    n = int(input())
    t = list(map(int, input().split()))
    a = [];
    c = 1
    for i in range(1, n):
        if t[i] != t[i - 1]:
            a.append(c)
            c = 1
        else:
            c += 1
    a.append(c)
    m = len(a)
    ans = 0
    for i in range(1, m):
        ans = max(ans, 2 * min(a[i - 1], a[i]))
    print(ans)
    return


t = 1
# t=int(input())
for _ in range(t):
    solve()
