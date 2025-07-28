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
    s = I()
    prev = s[0]
    cnt = 0
    ans = []
    for i in s:
        if prev == i:
            cnt += 1

        else:
            if cnt & 1 == 1:
                ans.append(prev)
            cnt = 1
            prev = i
    if cnt & 1 == 1:
        ans.append(prev)

    print(''.join(sorted(set(ans))))


