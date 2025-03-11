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
dic = {"Q": 9, "q": 9, "R": 5, "r": 5, "B": 3, "b": 3, "N":3, "n":3, "P":1, "p":1}

w = h = 0
for _ in range(8):
    s = I()
    for i in range(8):
        if s[i] in {'q', 'r', 'b', 'n', 'p'}:
            h += dic[s[i]]
        elif s[i] in {'Q', 'R', 'B', 'N', 'P'}:
            w += dic[s[i]]


if w == h:
    print("Draw")
elif w > h:
    print("White")
else:
    print("Black")