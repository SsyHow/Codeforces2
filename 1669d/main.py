import sys

input = sys.stdin.readline


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
for _ in range(a):
    b = II()
    s = I().strip().split('W')
    # print(s)
    for i in s:
        if len(i) == 1 or (len(i) == 2 and i[0] == i[1]):
            print("NO")
            break
        elif i and all(x == i[0] for x in i):
            print("NO")
            break
    else:
        print("YES")