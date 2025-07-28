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

    if b & 1 == 0:
        s1 = 0
        prev1 = L[0]
        for idx, i in enumerate(L[0::2]):
            if i < prev1:
                s1 = idx* 2
                prev1 = i
        s2 = 0
        prev2 = L[1]
        for idx, i in enumerate(L[1::2]):
            if i < prev2:
                s2 = idx*2 + 1
                prev2 = i
        # print(s1, s2)
        if prev1 > prev2 or (prev1 == prev2 and s1 > s2):
            print("Mike")
        else:
            print("Joe")
    else:
        print("Mike")
