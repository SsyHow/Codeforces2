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
L = LII()
ans = []
def find(x):
    v = set()
    while x not in v:
        v.add(x)
        x = L[x] - 1

    return x + 1
for i in range(a):
    ans.append(find(i))
print(*ans)