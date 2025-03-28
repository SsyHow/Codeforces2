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
a, b = MII()
L = []
for _ in range(a):
    L.append(list(I()))
f = True
for i in range(a):
    for j in range(b):
        if L[i][j] == 'W':
           if i > 0 and L[i-1][j] == "S" or \
               i < a - 1 and L[i+1][j] == "S" or \
               j > 0 and L[i][j-1] == 'S' or \
               j < b - 1 and L[i][j+1] == "S":
               f = False
if f:
    print("YES")
    for i in L:
        tmp = []
        for j in i:
            if j == '.':
                tmp.append("D")
            else:
                tmp.append(j)
        print(''.join(tmp))
else:
    print("NO")

