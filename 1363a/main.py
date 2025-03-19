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
    b, c = MII()
    L =LII()
    odd = even = 0
    for i in L:
        if i & 1 == 1:
            odd += 1
        else:
            even += 1

    for i in range(1, min(odd, c)+1, 2):
        # print(even, i, c)
        if even >= c - i:
            print("YES")
            break
    else:
        print("NO")