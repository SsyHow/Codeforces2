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
    k = f.readlines()
    s = 1 if k[0].strip() == 'front' else 0
    a = 0 if k[1].strip() == '1' else 1
    # print(k)
    with open('output.txt', 'w') as t:
        print('L' if s ^ a else 'R', file = t)

# s = 1 if I() == 'front' else 0
# a = 0 if II() == 1 else 1
# print('L' if s ^ a else 'R')