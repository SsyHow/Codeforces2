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
    M = [3, 1, 2, 1, 0, 1, 0, 0, 0, 0]

    for i in range(b):
        if M[L[i]] > 0 :
            M[L[i]] -= 1

        if all(j == 0 for j in M):
            print(i + 1)
            break
    else:
        print(0)