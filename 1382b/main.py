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

    if all(i == 1 for i in L):
        if b & 1 == 1:
            print("First")
        else:
            print("Second")

    else:
        cnt = 0
        for i in L:
            if i != 1:
               break
            cnt += 1

        if cnt & 1 == 1:
            print("Second")
        else:
            print("First")