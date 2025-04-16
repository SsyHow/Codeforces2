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

n, m = MII()
start = 1
L = []

for end in MII():
    L.append([start, end + start - 1])
    start = end + start
# print(L)
num = len(L)
r = 0
for k in MII():

    while r < num:
        if k > L[r][1]:
            r += 1
        else:
            print(r + 1, k - L[r][0] + 1)
            break

