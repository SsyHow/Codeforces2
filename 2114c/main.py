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
    prev = -1
    ans = 0
    tmp = 1
    for i in L:
        if i - prev >= 2:
            ans += (tmp + 1) // 2
            tmp = 1
        elif i - prev == 2:
            tmp += 1
        else:
            continue
        prev = i
    print(ans)