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
vowel = ['a', 'e', 'i', 'o', 'u']
a = II()
for _ in range(a):
    b = II()
    ans = []
    for i in range(5):
        tmp = vowel[i] * (b // 5)
        if b % 5 > i:
            tmp += vowel[i]
        ans.append(tmp)
    print(''.join(ans))

