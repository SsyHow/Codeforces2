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
from collections import Counter
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
def solve():
    n, c, d = MII()

    L = LII()
    x = min(L)
    dic = Counter(L)

    M = []
    for i in range(n):
        M.append(i * c + x)

    for i in M:
        for j in range(n):
            dic[d * j + i] -= 1
            if dic[d * j + i] < 0:
                print("NO")
                return
    else:
        print("YES" if all(dic[i] == 0 for i in dic) else 'NO')
for _ in range(a):
    solve()

