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
k = 0
p0 = 0
p1 = len(s) -1
while p0 < p1:

    if s[p0] != s[p1]:
        k += 1


    p0 += 1
    p1 -= 1
if (k == 0 and len(s) & 1 == 1) or (k == 1):
    print("YES")
else:
    print("NO")
