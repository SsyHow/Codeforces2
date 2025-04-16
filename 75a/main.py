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
a = I()
b = I()

s = a.replace('0', '')
t = b.replace('0', '')
k = str(int(a) + int(b)).replace('0', '')
if int(k) == int(s) + int(t):
    print("YES")
else: print("NO")
