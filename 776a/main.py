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
s1, s2 = I().split()
a = II()
print(s1, s2)
for _ in range(a):
    x1, x2 = I().split()
    if x1 == s1:
        s1 = x2
    if x1 == s2:
        s2 = x2
    print(s1, s2)

