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
s = sorted(list(I()))

ans = 0
p0 = 0
k = 0
prev = -2
while p0 < a and k < b:

    if ord(s[p0]) - ord('a') - prev >= 2:
        k += 1
        ans += ord(s[p0]) - ord('a') + 1
        prev = ord(s[p0]) - ord('a')
        p0 += 1
    else:
        p0 += 1
print(ans if k == b else -1)