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

def lcm(s1, s2):
    a = []
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            a.append(s1[i])
        else:
            break
    return ''.join(a)

a = II()
k = I()
for _ in range(a - 1):
    p = I()
    k = lcm(k, p)

print(len(k))

