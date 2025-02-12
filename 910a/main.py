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

i = 0
ans = 0

while i < a-1:
    tmp = 0

    # print(i)
    while s[i] != '1' and tmp < b:
        i -= 1
        tmp += 1

    if tmp == b:
        print(-1)
        break
    ans += 1
    i += b
else:
    print(ans)
