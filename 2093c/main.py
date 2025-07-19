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
def check(k):
    if k == 1:
        return False

    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return True

a = II()
for _ in range(a):
    b, c = MII()
    if b == 1 and check(int(str(b) * c)):
        print("YES")
    elif check(b) and c == 1:
        print("YES")
    else:
        print("NO")