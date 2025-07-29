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
t = II()
for _ in range(t):
    b = II()
    s1 = I()
    s2 = I()

    k1 = k2 = 0
    for i in range(b):
        if i & 1 == 0 and s1[i] == '1':
            k1 += 1
        elif i & 1 == 1 and s1[i] == '1':
            k2 += 1

    p1 = p2 = 0
    for i in range(b):
        if i & 1 == 1 and s2[i] == '0':
            p1 += 1
        elif i & 1 == 0 and s2[i] == '0':
            p2 += 1
    # print(k1,k2, p1, p2)
    print("YES" if k1 <= p1 and k2 <= p2 else "NO")
