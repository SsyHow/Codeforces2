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

s = I()

z = 0
for i in range(len(s)-1, -1, -1):
    if s[i] == '0':
        z += 1
    else:
        break

tmp = '0' * z + s
# print(tmp, tmp[::-1])
print("YES" if tmp == tmp[::-1] else "NO")

