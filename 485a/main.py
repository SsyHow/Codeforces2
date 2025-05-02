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

v = set()
a, m = MII()
# v.add(a)
while a%m not in v:
    v.add(a%m)

    if a%m == 0 :
        print("Yes")
        break
    a += a % m
else:
    print("No")