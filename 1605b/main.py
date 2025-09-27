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
    s = I()
    k = s.count('1')
    s2 = '0' * (b - k) + '1' * k
    ans = []
    for i in range(b):
        if s[i] != s2[i]:
            ans.append(i + 1)
    if ans:
        print(1)
        print(len(ans), *ans)
    else:
        print(0)