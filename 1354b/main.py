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
    b = I()
    l = 0
    dic = {}
    ans = float('inf')
    for r in range(len(b)):
        if b[r] not in dic:
            dic[b[r]] = 0
        dic[b[r]] += 1
        while len(dic) == 3:
            ans = min(ans, sum(dic.values()))
            dic[b[l]] -= 1

            if dic[b[l]] == 0:
                del dic[b[l]]
            l += 1
    print(ans if ans != float('inf') else 0)
