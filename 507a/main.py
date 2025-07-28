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
n, k = MII()
L = LII()

M = sorted(zip(L, range(1, n + 1)))
cnt = 0
tmp = 0
ans = []
for i in M:
    if cnt + i[0] > k:
        break

    cnt += i[0]
    tmp += 1
    ans.append(i[1])
print(tmp)
print(*ans)



