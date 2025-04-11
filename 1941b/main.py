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
    for i in range(b - 2):
        if L[i] > 0:

            L[i + 1] -= L[i] * 2
            L[i + 2] -= L[i]
            L[i] -= L[i]
            # print(L)
            if L[i + 1] < 0 or L[i + 2] < 0:
                print("NO")
                break
    else:
        print("YES" if L[-1] == L[-2] == 0 else "NO")