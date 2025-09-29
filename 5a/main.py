import sys
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
dic = set()
ans = 0
for s in sys.stdin:
    s = s.strip()
    if s[0] == '+':
        dic.add(s[1:])

    elif s[0] == '-':
        dic.remove(s[1:])

    else:
        _, x = s.split(':')
        ans += len(x) * len(dic)
print(ans)
