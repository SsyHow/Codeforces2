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
a, b = MII()
dic = {}
for _ in range(b):
    s1, s2 = I().split()
    dic[s1] = s2 if len(s2) < len(s1) else s1
    dic[s2] = s2 if len(s2) < len(s1) else s1

L = LI()

for i in range(a):
    L[i] = dic[L[i]]
print(" ".join(L))
