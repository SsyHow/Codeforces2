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
    L = [0] + LII()
    M = [0] * (b+1)
    ans = []
    if b == 1:
        print(-1)
        continue
    for i in range(1, b-1):
        k = 1
        while M[k] or k == L[i]:
            k += 1
        ans.append(k)
        M[k] = 1
    x = b
    a = b = -1
    for i in range(1, x+1):

        if M[i] == 0:
            if a == -1:
                a = i
            else:
                b = i
    if a != L[-2] and b != L[-1]:
        ans.append(a)
        ans.append(b)
    else:
        ans.append(b)
        ans.append(a)
    print(*ans)

