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
    st = 1
    en = 1
    L = [0] + L + [0]
    while st < b and L[st] <= L[st + 1]:
        st += 1

    while en < b and L[b - en] >= L[b - en + 1]:
        en += 1
    # print(st, en)
    if st + en >= b:
        print("YES")
    else:
        print("NO")
