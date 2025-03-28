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

b = I()
k = set(list(b))
s = set()
ans = 0
ans += (len(b) + 1) * (26 - len(k))

for i in k:
    for j in range(0, len(b)+1):
        s.add(b[:j] + i + b[j:])
print(ans + len(s))