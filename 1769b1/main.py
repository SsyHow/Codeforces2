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
n = II()
sp = LII()
sp1 = []

for i in range(n):
    for j in range(sp[i]):
        if ((100 * j) // sp[i]) == (100 * (sum(sp[:i]) + j) // (sum(sp))):
            sp1.append(((100 * j) // sp[i]))
print(*sorted(set(sp1)), 100, sep='\n')