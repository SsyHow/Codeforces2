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
L = []
for _ in range(a):
    L.append(LII())

L.sort(key = lambda x: (x[0], x[1]))

if a == 1:
    print("Poor Alex")
else:
    for i in range(a - 1):
        if L[i][1] > L[i + 1][1]:
            print("Happy Alex")
            break
    else:
        print("Poor Alex")