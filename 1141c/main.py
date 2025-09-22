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
L = LII()
vis = {0}
M = [0]
for i in L:
    k = i + M[-1]
    if k in vis:
        print(-1)
        break
    vis.add(k)
    M.append(k)
else:
    mn = min(M)
    mx = max(M)
    if mx - mn > a - 1 :
        print(-1)
    else: print(*[i + 1 - mn for i in M])

