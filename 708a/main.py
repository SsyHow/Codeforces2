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
s = I()
ans = []
if any(i != 'a' for i in s):

    f = True
    ff = True
    for i in s:
        if f:
            if ff and i == 'a':
                ans.append('a')
            elif i == 'a':
                ans.append('a')
                f = False
            else:
                ans.append(chr(ord(i) - 1))
                ff = False
        else:
            ans.append(i)
    print(''.join(ans))
else:
    print(s[:-1] + 'z')