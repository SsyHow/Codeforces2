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
n, d = MII()
L = LII()

ans = prev = 0

for i in L:

    if i == prev:
        ans += 1
        prev += d
    elif i < prev:
        ans += (prev - i)// d + 1
        prev = i +  ((prev - i)// d + 1) * d
    else:
        prev = i
print(ans)