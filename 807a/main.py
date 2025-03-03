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
rate = False
Maybe = False
prev = float('inf')
for _ in range(a):
    b, c = MII()
    if not rate and b != c:
        rate = True
    if not Maybe and b > prev:
        Maybe = True
    prev = b

if rate:
    print("rated")
elif not Maybe:
    print("maybe")
else:
    print("unrated")
