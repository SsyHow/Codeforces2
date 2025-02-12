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

s = 'heidi'

a = I()
p = 0

for i in range(len(a)):
    if a[i] == s[p]:
        p += 1
    if p == 5 :
        break
if p == 5:
    print("YES")
else:
    print("NO")
