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
    # L.append(float('inf'))
    L.sort()
    L = [-1] + L + [b + 2]
    ans = 0
    for i in range(b+1):
        # print(i, L[i], L[i + 1])
        if i > L[i] and i < L[i + 1]:
            # print(i, L[i], L[i + 1])
            ans += 1
    print(ans)
