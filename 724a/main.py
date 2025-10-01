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
dic = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
k = dict(zip(dic, range(7)))
a = I()
b = I()
for i in {28, 30, 31}:
    if (k[a] + i) % 7 == k[b]:
        print("YES")
        break
else:
    print("NO")