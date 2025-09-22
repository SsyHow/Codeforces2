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

def foo(x, L1, L2):
    s, e = 0, x-1
    for i in L1:
        if i == L2[s]:
            s += 1
        elif i == L2[e]:
            e -= 1
        else:
            return False
    return True

t = II()
for _ in range(t):
    b = II()
    L1 = LII()
    L2 = LII()

    print("Bob" if foo(b, L1, L2) and foo(b, L1[::-1], L2) else "Alice")

