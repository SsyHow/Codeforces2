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
    s = list(I())
    tmp = ''
    for i in range(len(s) - 2, 0, -1):
        if s[i] != '0' and s[i + 1] != '0':
            if int(s[i]) + int(s[i + 1]) > 9:
                s[i] = str(int(s[i]) + int(s[i + 1]))
                s[i + 1] = ''
                print(''.join(s))
                break
    else:
        s[0] = str(int(s[0]) + int(s[1]))
        s[1] = ''
        print(''.join(s))

