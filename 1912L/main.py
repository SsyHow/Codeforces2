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
s = I()

for i in range(1, a):
    s1 = s[:i]
    s2 = s[i:]

    ls1 = s1.count('L')
    ls2 = s2.count('L')
    os1 = s1.count('O')
    os2 = s2.count('O')
    # print(s1, s2, ls1, ls2, os1,os2)
    if ls1 != ls2 and os1 != os2:
        print(i)
        break
else:
    print(-1)