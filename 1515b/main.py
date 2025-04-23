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
def check(k):
    if int(k ** 0.5) ** 2 == k:
        return True
    return False

t = II()
for _ in range(t):
    a = II()
    x = y = False
    if a % 2 == 0 and check(a // 2):
        x = True

    if a % 4 == 0 and check(a// 4):
        y = True
    print("YES" if x or y else "NO")
