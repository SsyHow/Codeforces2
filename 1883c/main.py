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
    n, k = MII()
    L = LII()
    cnto = cnte = 0
    if k == 4:
    #     print(max(min(k - i % k if i % k > 0 else 0 for i in L) - 1, 0))
    # else:
        M = Counter( i%k if i%k > 0 else 0 for i in L)

        if M[0] > 0 or M[2] > 1:
            print(0)
        elif M[3] > 0 or (M[2] == 1 and M[1] > 0):
            print(1)
        else:
            print(2)
        # print(M)
        # print(L)
        # print([i%k if i%k > 0 else 0 for i in L])
    else:
        print(min(k - i%k if i%k > 0 else 0 for i in L))