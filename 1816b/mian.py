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
    even = list(range(2, b*2 + 1, 2))
    odd = list(range(1, b*2, 2))
    ans = [[],[]]
    s1, s2 = 0, b - 1
    while s1 < s2:
        ans[0].append(even[s2])
        ans[0].append(even[s1])
        s1 += 1
        s2 -= 1
    s1, s2 = 0, b//2
    while s2 < b :
        ans[1].append(odd[s1])
        ans[1].append(odd[s2])
        s1 += 1
        s2 += 1
    for i in ans:
        print(*i)