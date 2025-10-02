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

ans = 0
while a > 1:
    ans += a
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            a //= i
            break
    else:
        a = 1
print(ans + 1)