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
from collections import Counter
a = II()
for _ in range(a):
    b = II()
    L = LII()

    c = Counter(L)

    x = sorted(c.items(), key=lambda x: x[1])
    flag = True
    ans = 0
    for i in x:
        if i[1] > 1:
            ans += 1
        if flag:
            if i[1] == 1:
                ans += 2


        flag = not flag
    print(ans)


