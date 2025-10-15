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
    b, c = MII()
    s1 = I()
    s2 = I()

    L = [0] * 26
    M = []
    M.append([0] * 26)
    for i in range(b):
        # print(ord(s1[i]) - ord('a'))
        L[ord(s1[i]) - ord('a')] += 1
        L[ord(s2[i]) - ord('a')] -= 1
        M.append(L.copy())

    # print(M)
    for i in range(c):
        x, y = MII()
        tmp = 0
        for j in range(26):
            tmp += abs(M[y][j] - M[x- 1][j])
        print(tmp // 2)
