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
s = I()
L = []
for i in range(0, 80, 10):
    L.append(s[i:i+10])
dic = {}
for i in range(10):
    dic[I()] = i

ans = []
for i in L:
    ans.append(dic[i])
print(*ans, sep='')