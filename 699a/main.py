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
b = II()
s = I()
L = LII()
tmp = float('inf')
for i in range(b - 1):
    if s[i] == 'R' and s[i + 1] == 'L':
        tmp = min((L[i + 1] - L[i]) // 2, tmp)
print(tmp if tmp != float('inf') else -1)
