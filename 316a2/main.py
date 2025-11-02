import sys

input = lambda: sys.stdin.readline().rstrip()


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
def f(n, a):
    ans = 1
    k = 10

    while n > 0:
        ans *= k
        k -= 1
        n -= 1
    if a == 1:
        ans //= 10
        ans *= 9
    return ans
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
s = I()
ans = 1
ss = set()
x = 0
for i in range(len(s)):
    if s[i] in '0123456789':
        continue
    if s[i] == '?' and i != 0 :
        x += 1
    elif s[i] == '?' and i == 0 :
        ans *= 9
    else:
        ss.add(s[i])
# print(s[0] in ss)
print(ans * f(len(ss), 0) if s[0] not in ss or s[0] == '?' else ans * f(len(ss), 1), '0' * x, sep = '')