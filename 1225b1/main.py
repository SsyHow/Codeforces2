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
    n, k, d = MII()
    L = LII()
    dic = {}
    for i in range(d):
        if L[i] not in dic:
            dic[L[i]] = 0
        dic[L[i]] += 1
    ans = len(dic)
    for i in range(d, n):
        if L[i] not in dic:
            dic[L[i]] = 0
        dic[L[i]] += 1
        dic[L[i - d]] -=1
        if dic[L[i - d]] == 0:
            del dic[L[i-d]]
        ans = min(len(dic), ans)
    print(ans)
