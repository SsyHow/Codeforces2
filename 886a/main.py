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
L = LII()
x = sum(L)
def check(L):
    for i in range(6):
        for j in range(i + 1, 6):
            for k in range(j + 1, 6):
                l = L[i] + L[j] + L[k]
                if x - l == l:
                    return "YES"
    return "NO"

print(check(L))