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
with open('input.txt', 'r') as f:
    f = f.readlines()
    a, b = map(int, f[0].split())

    L = list(map(int, f[1].split()))

    k = sorted(zip(L, range(1, a + 1)))
    with open('output.txt', 'w') as t:
        print(k[-b][0], file= t)
        for i in k[-b:]:

            print(i[1], end = ' ', file= t)
        print(file= t)
