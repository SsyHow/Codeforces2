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
c, v0, v1, a, l = MII()

cnt = 0
sped = 0
ans = 0
while cnt < c:
    cnt += min(v0 + sped * a, v1)
    sped += 1
    ans += 1
    if cnt >= c:
        break
    cnt -= l
print(ans)