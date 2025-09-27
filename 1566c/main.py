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
    s1 = I()
    s2 = I()
    ans = 0
    i = 0
    while i < b:

        if (s1[i] == '0' and s2[i] == '1') or (s1[i] == '1' and s2[i] == '0'):
            ans += 2
            i += 1

        elif i < b - 1:
            if (s1[i] == s2[i] == '1') and (s1[i + 1] == s2[i + 1] == '0'):
                ans += 2
                i += 1
            elif (s1[i] == s2[i] == '0') and (s1[i + 1] == s2[i + 1] == '1'):
                ans += 2
                i += 1
            elif (s1[i] == s2[i] == '0'):
                ans += 1
            i += 1
        else:
            if (s1[i] == s2[i] == '0'):
                ans += 1
            i += 1
    print(ans)

