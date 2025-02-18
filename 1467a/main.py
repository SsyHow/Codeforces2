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
    s = 0
    ans = ['989']
    if b == 1:
        print(9)
    elif b == 2:
        print(98)
    elif b == 3:
        print(989)

    else:
        for i in range(b-3):
            ans.append(str(s))
            s = s + 1 if s < 9 else 0
        print(''.join(ans))