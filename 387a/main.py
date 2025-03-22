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
a1, a2 = map(int, (I().split(':')))
b1, b2 = map(int, (I().split(':')))

if a2 - b2 < 0:
    a1 -= 1

print(str((a1-b1)%24).zfill(2) , ':' , str((a2-b2)%60).zfill(2), sep='')

