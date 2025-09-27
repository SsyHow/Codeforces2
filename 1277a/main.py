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
for i in range(a):
    b = II()
    tmpb = b
    k = 1
    zz = 0
    while b > 10:
        k *= 10
        k +=1
        b //= 10
        zz += 1


    ans = 0
    x = k
    cnt = 1
    while k <= tmpb and cnt < 10 :
        k += x
        ans += 1
        cnt += 1
    ans += zz * 9
    print(ans)