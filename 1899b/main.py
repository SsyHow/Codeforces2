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
for _ in range(II()):
    b = II()
    L = LII()
    ans = 0
    for i in range(1, b // 2 + 1):
        if b % i == 0:
            tmpmx = 0
            tmpmn = float('inf')
            # print(i)
            for j in range(0, b, i):
                # print(L[j : i], sum(L[j : i]))
                tmpmx = max(tmpmx, sum(L[j:j + i]))
                tmpmn = min(tmpmn, sum(L[j:j + i]))
        ans = max(ans, tmpmx - tmpmn)
    print(ans)
