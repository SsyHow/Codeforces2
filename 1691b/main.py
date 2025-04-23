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

    cnt = 0
    prev = L[0]
    ans = []
    f = True
    for idx, i in enumerate(L):
        if i != prev:
            if cnt == 1:
                f = False
                break
            ans.append(idx)
            for j in range(idx - cnt + 1, idx):
                ans.append(j)

            cnt = 1
            prev = i
        else:
            cnt += 1
    if cnt == 1:
        f = False
    else:
        ans.append(idx + 1)
        for j in range(idx - cnt + 2, idx + 1):
            ans.append(j)


    print(*ans if f else [-1])
