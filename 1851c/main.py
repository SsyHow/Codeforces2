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
    if L[0] == L[-1]:
        print("YES" if L.count(L[0]) >= k else "NO")

    else:
        cnt1 = cnt2 = p0 = 0
        p1 = n- 1
        while p0 < n and cnt1 < k:
            if L[p0] == L[0]:
                cnt1 += 1
                if cnt1 == k:
                    break
            p0 += 1
        while p1 > 0 and cnt2 < k:
            if L[p1] == L[-1]:
                cnt2 += 1
                if cnt2 == k:
                    break
            p1 -= 1
        # print(cnt1, cnt2)
        print("YES" if p0 < p1 else "NO")

