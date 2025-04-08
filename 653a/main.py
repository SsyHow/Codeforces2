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
L = sorted(set(MII()))

for i in range(1, len(L) -1):
    if 0 < L[i] - L[i-1] < 2 and 0 < L[i + 1] - L[i] < 2 :
        # print(L[])
        print("YES")
        break
else:
    print("NO")