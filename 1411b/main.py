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

def check(i):
    k = set(str(i))
    for x in k:
        if int(x) == 0:
            continue
        if i % int(x) != 0:
            return True
    return False

a = II()
for _  in range(a):
    b = II()
    while check(b):
        b += 1
    print(b)