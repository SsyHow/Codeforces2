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
L = LII()
count = 0
mx = -1
o = 0
for i in L:
    if i == 0:
        count += 1
        mx = max(mx, count)
    else:
        if count > 0:
            count -= 1
        o += 1
if a == 1:
    if L[0] == 0:
        print(1)
    else:
        print(0)
elif o == a:
    print(a - 1)
else:
    print(o + mx)
