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

s1 = I()
s2 = I()

L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
def find(x):
    k = [0,0]
    for idx, i in enumerate(L, start = 1):
        if x[0] == i:
            k[0] = idx
            break
    k[1] = int(x[1])

    return k

co1 = find(s1)
co2 = find(s2)
ans = []
while co1 != co2:
    tmp = []
    if co1[0] > co2[0]:
        tmp.append('L')
        co1[0] -= 1
    elif co1[0] < co2[0]:
        tmp.append('R')
        co1[0] += 1

    if co1[1] > co2[1]:
        co1[1] -= 1
        tmp.append('D')
    elif co1[1] < co2[1]:
        co1[1] += 1
        tmp.append('U')
    ans.append(''.join(tmp))
print(len(ans))
print(*ans, sep='\n')
