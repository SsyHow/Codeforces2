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
s = s + '.'
L = []

prev = s[0]
cnt = 0

for i in s:
    if prev == i:
        cnt += 1
    else:
        L.append((prev, cnt))
        cnt = 1
        prev = i
k = len(L)
if k & 1 == 0:
    print(0)
elif L[k//2][1] == 1:
    print(0)
elif any(L[i][0] != L[k-i-1][0] or L[i][1] + L[k-i-1][1] < 3 for i in range(k // 2)):
    print(0)
else:
    print(L[k//2][1] + 1)