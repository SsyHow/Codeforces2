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
p0 = 0
p1 = a- 1
s = I()
ans = 0

while p0 < a and s[p0] == '<':
    p0 += 1
while p1 > - 1 and s[p1] == '>':
    p1 -= 1

print(p0 + a - p1 - 1)




