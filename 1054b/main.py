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
vis = set()
mex = 0
k = 1
for i in L:
    if i not in vis and i != mex:
        print(k)
        break

    k +=1
    if i not in vis:
        mex += 1
    vis.add(i)
else:
    print(-1)