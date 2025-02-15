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
    n, f, a, b = MII()
    L = LII()
    t = 0
    L = [0] + L
    for i in range(1, n+1):
        t += min((L[i] - L[i-1] ) * a, b)
        # print(t, f)
        if t >= f:
            print("NO")
            break
    else:
        print("YES")
