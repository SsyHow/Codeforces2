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
    b, s = I().split()
    b = int(b)
    L = list(I() * 2)
    sarr = [i for i in range(b*2) if L[i] == s]
    garr = [i for i in range(b*2) if L[i] == 'g']
    if s == 'g':
        print(0)
        continue
    ans = 0
    p1 = 0
    for x in sarr:
        while p1 < len(garr) and garr[p1] < x:
            p1 += 1
        if p1 < len(garr):
            ans = max(ans, garr[p1] - x)
    print(ans)

    # print(sarr)
    # print(garr)