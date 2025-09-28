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
n = len(s)
ans = 0
pre = -1
i = 0
while i < n - 3:
    if s[i: i + 4] == 'bear':
        ans += (i - pre) * (n - 3 - i)
        pre = i
        i += 3
    i += 1
print(ans)
