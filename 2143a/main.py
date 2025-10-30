import sys

input = lambda: sys.stdin.readline().rstrip()


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
for _ in range(a):
    b = II()
    L = LII()

    l = r = L.index(b)
    k = b
    while l >= 0 and r <= b - 1:
        if l > 0  and L[l - 1] == k - 1:
            l -= 1
            k -= 1
        elif r < b - 1 and L[r + 1] == k - 1:
            r += 1
            k -= 1
        else:
            break

    print("YES" if l == 0 and r == b-1 else "NO")
