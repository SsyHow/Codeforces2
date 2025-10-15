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
f = True
L = [''] * len(a)
for i in range(len(a)):
    if f and a[i] == '0':
        f = False
        continue
    else:
        L[i] = a[i]
# print(L)
if f:
    L.pop()

print(''.join(L))