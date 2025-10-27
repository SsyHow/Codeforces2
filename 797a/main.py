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
def solve():
    n, k = MII()

    L = []
    i = 2
    if k > 1:
        while k:

            while n % i == 0:
                L.append(i)
                n //= i
                k -= 1
                if k == 1 and n > 1:
                    print(*L, n)
                    return
            i += 1
            if i > n:
                break
        print(-1)
    else:
        print(n)
solve()
