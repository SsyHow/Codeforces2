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
    if b == 3:
        print("NO")
    elif b & 1 == 0:
        print("YES")
        print(*([1,-1] * (b // 2)))
    else:
        print("YES")
        print(*([(b+1)//2 - 2,-(b//2)] *(b//2) + [(b+1)//2 - 2]) )