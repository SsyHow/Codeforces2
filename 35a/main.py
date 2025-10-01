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
    a = int(f.readline())
    for _ in range(3):
        x, y = map(int, f.readline().split())
        if a != x and a != y:
            continue
        elif a == x:
            a = y
        elif a == y:
            a = x
    with open('output.txt', 'w') as t:
        print(a, file = t)