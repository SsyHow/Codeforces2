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
    s = I()
    M = []
    sm = 0
    for i in range(b):
        if s[i] == 'L':
            k = 0
        else:
            k = 1

        L = [i, b - i - 1]
        M.append(max(L) - L[k])
        sm += max(L)
    M.sort()
    # print(M)
    ans = []
    for i in M:
        ans.append(sm)
        sm -= i
    print(*ans[::-1])
