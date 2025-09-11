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

    odd = []
    even = []
    for i in L:
        if i & 1 == 1:
            odd.append(i)
        else:
            even.append(i)

    if not odd:
        print(max(even))
    elif not even:
        print(max(odd))
    else:
        print(sum(L) - len(odd) + 1)
