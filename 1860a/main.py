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
    s = I()
    n = len(s)
    a = '()' * (n)
    b = '(' * (n) + ')' * (n)
    if s not in a :
        print("YES")
        print(a)
    elif s not in b:
        print("YES")
        print(b)
    else:
        print("NO")
