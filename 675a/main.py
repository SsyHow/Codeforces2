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
a, b, c = MII()
if c == 0:
    print("YES" if a == b else "NO")
elif a <= b and c > 0 and  (b - a) % c == 0:
    print("YES")
elif b <= a and c < 0 and (a - b) % c == 0:
    print("YES")
else:
    print("NO")
