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

s = I()
flag = False


UP = LO = dig = False

for i in s:
    if 'a' <= i <= 'z':
        LO = True
    elif 'A' <= i <= 'Z':
        UP = True
    elif '0' <= i <= '9':
        dig = True


if len(s) >= 5 and UP and LO and dig:
    print("Correct")
else:
    print("Too weak")