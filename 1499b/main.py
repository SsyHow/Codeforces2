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
    s = I()
    f = False
    for i in range(len(s) - 1):
        if s[i] == '1' and s[i + 1] == '1':
            f = True

        if f and s[i] == '0' and s[i + 1] == '0':
            print("NO")
            break
    else:
        print("YES")