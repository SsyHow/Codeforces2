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

def check(t, u):
    if t == u:
        return 0, 0

    a = b = 0
    k1 = t
    while t != u:
        t += 1
        t %= 26
        a += 1
    while k1 != u:
        k1 -= 1
        k1 %= 26
        b += 1
    return a, b
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
s = I()
ans = float('inf')
for i in range(a - 3):
    tmp = 0
    tmp += min(check(ord(s[i]) - ord('A') , ord('A') - ord('A')))
    tmp += min(check(ord(s[i + 1]) - ord('A') , ord('C') - ord('A')))
    tmp += min(check(ord(s[i + 2]) - ord('A') , ord('T') - ord('A')))
    tmp += min(check(ord(s[i + 3]) - ord('A') , ord('G') - ord('A')))
    ans = min(ans, tmp)
print(ans)