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


dic = {1: "Sheldon", 2: "Leonard", 3:"Penny", 4:"Rajesh", 5:"Howard"}
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()

x = 1
cnt = 0
while a - x * 5 > 0:

    a -= x * 5
    x += x
    cnt += 1

k = 1
while a > x * k:
    k += 1
print(dic[k])
