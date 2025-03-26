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
f = True
k = set(list('aeiou'))
for i in s:
    if not f and i not in k:
        print("NO")
        break
    if i not in k and i != 'n':
        f = False
    else:
        f = True
else:
    print("YES" if f else "NO")