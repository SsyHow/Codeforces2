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

    M = []
    for i in L:

        if not M or i != M[-1]:
            M.append(i)
    ans = 0
    n = len(M)
    if n == 1:
        print("YES")
        continue

    for i in range(n):
        if i == 0 and M[i] < M[i + 1]:
            ans += 1
        elif i == n - 1 and M[i - 1] > M[i]:
            ans += 1
        elif 0 < i < n - 1 and M[i-1] > M[i] and M[i + 1] >  M[i]:
            ans += 1
    print("YES" if ans == 1 else "NO")
