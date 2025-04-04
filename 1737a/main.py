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
from collections import Counter
a = II()
for _ in range(a):
    b, x = MII()
    s = I()
    c = Counter(s)
    ans = []
    for _ in range(x):
        for i in range(26):
            if c[chr(i + ord('a'))] == 0 or i == b // x:
                ans.append(chr(i + ord('a')))
                break
            else:
                c[chr(i + ord('a'))] -= 1
    print(''.join(ans))



