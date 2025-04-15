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

from collections import defaultdict

a = II()
for _ in range(a):
    b = II()
    L = LII()
    L = [i + 1 for i in L]
    c = II()
    for _ in range(c):
        x = defaultdict(int)
        y = defaultdict(str)
        s = I()

        if len(s) != b:
            print("NO")
            continue
        for i in s:
            x[i] = float('inf')

        for i in range(b):
            if x[s[i]] != float('inf') and x[s[i]] != L[i]:
                print("NO")
                break
            x[s[i]] = L[i]

            if y[L[i]] != '' and y[L[i]] != s[i]:
                print("NO")
                break
            y[L[i]] = s[i]
        else:
            print("YES")


