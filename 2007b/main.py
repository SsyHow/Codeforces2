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
    b, c = MII()
    L = LII()
    k = max(L)
    ans = []
    for _ in range(c):

        s, x, y = I().split()
        x, y = int(x), int(y)
        if x <= k <= y:
            if s == '+':
                k += 1
            else:
                k -= 1

        ans.append(k)

    print(* ans)
