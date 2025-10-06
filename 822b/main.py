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
a, b = MII()
s = I()
t = I()

k = float('inf')
ll = []
for i in range(b - a + 1):
    tmp = []
    for j in range(a):
        if s[j] != t[i + j]:
            tmp.append(j + 1)

    if len(tmp) < k:
        k = len(tmp)
        ll = tmp.copy()

print(k)
print(*ll)
