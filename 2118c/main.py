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
    n, k = MII()
    L = LII()

    cnt = [0] * 60
    ans = 0

    for v in L:
        ans += v.bit_count()
        for i in range(60):
            cnt[i] += 1 if (v >> i) & 1 == 0 else 0

    for i in range(60):
        need = cnt[i]
        mx = k >> i

        if mx <= need:
            ans += mx
            break
        else:
            ans += need
            k -= need << i
    print(ans)
